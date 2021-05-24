
package body Node is

    task body NodeStash is
        stash: pMessage := null;

        exitTask: Boolean := False;
    begin
        loop
            select
                accept SendMessage(message: pMessage) do
                    stash := message;
                end SendMessage;
                or
                accept Stop do
                    exitTask := True;
                end Stop;
            end select;
            if stash /= null then
                self.all.receiverTask.all.GetMessage(stash);
                stash := null;
            end if;
            if exitTask then
                exit;
            end if;
        end loop;
    end NodeStash;

    task body NodeTaskGrimReaper is
    begin
        node.all.senderTask.all.Stop;
        node.all.receiverTask.all.Stop;
        node.all.stash.all.Stop;
    end NodeTaskGrimReaper;

    task body ReceiverTask is
        tmpOffer: pOffer;
        newCost: Natural := 0;
        id: Natural := 0;

        internalStash: pMessage;

        exitTask: Boolean := False;
    begin
        loop
            select
                accept GetMessage(tmpMessage: pMessage) do
                    internalStash := tmpMessage;
                end GetMessage;
            or
                accept Stop do
                    exitTask := True;
                end Stop;
            end select;
            if exitTask then
                exit;
            end if;
            -- apply all offers
            for j in internalStash.all.contents.all'Range loop
                tmpOffer := internalStash.all.contents.all(j);
                if tmpOffer /= null then
                    id := tmpOffer.all.id;
                    newCost := 1 + tmpOffer.all.currentCost;

                    if id /= self.all.id and newCost < self.all.routing.cost(id) then
                        logger.Log("→→→offer from node" & Natural'Image(internalStash.all.sender.all.id) & " accepted by node" & Natural'Image(self.all.id) & ": found better path to node" & Natural'Image(id) & " (cost" & Natural'Image(tmpOffer.all.currentCost) & "+1)");
                        self.all.routing.cost(id) := newCost;
                        self.all.routing.nextHop(id) := internalStash.all.sender;
                        self.all.routing.changed(id) := True;
                    end if;
                end if;
            end loop;
        end loop;
    end ReceiverTask;

    task body SenderTask is
        subtype RangeN is Natural range 1..n;

        tmpMessage: pMessage;
        tmpOffer: pOffer;
        anythingToSend: Boolean := False;

        exitTask: Boolean := False;
    begin
        loop
            select
                accept Stop do
                    exitTask := True;
                end Stop;
            else
                SleepForSomeTime(maxSleep);

                tmpMessage := new Message;
                tmpMessage.all.contents := new Array_pOffer(RangeN);
                tmpMessage.all.sender := self;

                for j in RangeN'Range loop
                    if j /= self.all.id and self.all.routing.changed(j) then
                        self.all.routing.changed(j) := False;

                        tmpOffer := new Offer;
                        tmpOffer.all.id := j;
                        tmpOffer.all.currentCost := self.all.routing.cost(j);

                        logger.Log("new offer from node" & Natural'Image(self.all.id) & ": potentially better path to node" & Natural'Image(tmpOffer.all.id) & " (cost" & Natural'Image(tmpOffer.all.currentCost) & ")");
                        tmpMessage.all.contents(j) := tmpOffer;
                        anythingToSend := True;
                    end if;
                end loop;

                if anythingToSend then
                    for i in self.all.neighbours'Range loop
                        self.all.neighbours(i).all.stash.SendMessage(tmpMessage);
                    end loop;
                    anythingToSend := False;
                end if;
            end select;
            if exitTask then
                exit;
            end if;
        end loop;
    end SenderTask;

end Node;

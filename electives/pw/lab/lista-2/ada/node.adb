
package body Node is

    procedure SleepForSomeTime (maxSleep: Natural; intervals: Natural := 1) is
       gen: RAF.Generator;
       fraction: Float;
    begin
       RAF.Reset(gen);
       fraction := 1.0 / Float(maxSleep);
       delay Duration(fraction * RAF.Random(gen) * Float(intervals));
    end SleepForSomeTime;

    task body NodeTask is
        target: pNodeObj;
        neighbours: pArray_pNodeObj;
        stash: pMessage;

        exitTask: Boolean := False;

        trapActive: Boolean := False;

    begin
        loop
            select
                accept SendMessage(message: in pMessage) do
                    logger.LogMessageInTransit(message.all.content, self.all.id);
                    stash := message;

                    if trapActive then
                        logger.Log("→→→ message" & Natural'Image(stash.all.content) & " fell into plunderer’s trap");
                        stash := null;
                        receiver.all.ReceiveMessage;
                        trapActive := False;
                    end if;

                    SleepForSomeTime(maxSleep);

                    if stash /= null and isLast then
                        -- allow receiving the message only if the node is the last node
                        logger.Log("→→→ message" & Natural'Image(stash.all.content) & " received");
                        stash := null;
                        receiver.all.ReceiveMessage;
                    end if;

                    if stash /= null then
                        stash.all.health := Natural'Pred(stash.all.health);
                        if stash.all.health = 0 then
                            -- message has exhausted its health
                            logger.Log("→→→ message" & Natural'Image(stash.all.content) & " died of exhaustion");
                            stash := null;
                            receiver.all.ReceiveMessage;
                        end if;
                    end if;
                    -- logger.Log("message" & Natural'Image(message.all.content) & " has" & Natural'Image(message.all.health) & " health" & " node" & Natural'Image(self.all.id));
                end SendMessage;
                or
                accept SetupTrap do
                    trapActive := True;
                end SetupTrap;
                or
                accept Stop do
                    exitTask := True;
                end Stop;
            else
                SleepForSomeTime(maxSleep);
            end select;
            if stash /= null then
                neighbours := self.all.neighbours;
                target := neighbours.all(RAD.Next(neighbours'Length));
                -- logger.Log("message" & Natural'Image(stash.all.content) & " is about to be sent from node" & Natural'Image(self.all.id) & " to node" & Natural'Image(target.all.id));
                target.all.nodeStash.all.SendMessage(stash);
                -- logger.Log("message" & Natural'Image(stash.all.content) & " sent from node" & Natural'Image(self.all.id) );
                stash := null;
            end if;
            if exitTask then
                exit;
            end if;
        end loop;
    end NodeTask;

    task body NodeStash is
        exitTask: Boolean := False;

        stash: pMessage;
    begin
        loop
            select
                accept SendMessage(message: in pMessage) do
                    stash := message;
                end SendMessage;
                or
                accept Stop do
                    exitTask := True;
                end Stop;
            end select;
            if stash /= null then
                self.all.nodeTask.all.SendMessage(stash);
                stash := null;
            end if;
            if exitTask then
                exit;
            end if;
        end loop;
    end NodeStash;

    task body NodeTaskGrimReaper is
    begin
        node.all.nodeTask.Stop;
        node.all.nodeStash.Stop;
    end NodeTaskGrimReaper;

end Node;

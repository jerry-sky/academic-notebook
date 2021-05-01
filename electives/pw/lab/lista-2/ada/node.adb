
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
                        receiver.all.ReceiveMessage;
                        stash := null;
                        trapActive := False;
                    end if;

                    SleepForSomeTime(maxSleep);

                    if stash /= null and isLast then
                        -- allow receiving the message only if the node is the last node
                        logger.Log("→→→ message" & Natural'Image(stash.all.content) & " received");
                        receiver.all.ReceiveMessage;
                        stash := null;
                    end if;

                    if stash /= null then
                        stash.all.health := Natural'Pred(stash.all.health);
                        if stash.all.health = 0 then
                            -- message has exhausted its health
                            logger.Log("→→→ message" & Natural'Image(stash.all.content) & " died of exhaustion");
                            receiver.all.ReceiveMessage;
                            stash := null;
                        end if;
                    end if;
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
                target.all.nodeTask.all.SendMessage(stash);
                stash := null;
            end if;
            if exitTask then
                exit;
            end if;
        end loop;
    end NodeTask;

    task body NodeTaskGrimReaper is
    begin
        node.all.nodeTask.Stop;
    end NodeTaskGrimReaper;

end Node;

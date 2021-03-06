
package body Node is

    procedure SleepForSomeTime (maxSleep: Natural) is
       gen: RAF.Generator;
       fraction: Float;
    begin
       RAF.Reset(gen);
       fraction := 1.0 / Float(maxSleep);
       delay Duration(fraction * RAF.Random(gen));
    end SleepForSomeTime;

    task body NodeTask is
        target: pNodeObj;
        neighbours: pArray_pNodeObj;
        stash: pMessage;

        exitTask: Boolean := False;

    begin
        loop
            select
                accept SendMessage(message: in pMessage) do
                    logger.LogMessageInTransit(message.all.content, self.all.id);
                    SleepForSomeTime(maxSleep);
                    stash := message;
                    if isLast then
                        -- allow receiving the message only if the node is the ending node
                        accept ReceiveMessage(message: out pMessage) do
                            -- hand over the message
                            message := stash;
                            stash := null;
                        end ReceiveMessage;
                    end if;
                end SendMessage;
                or
                accept Stop do
                    SleepForSomeTime(maxSleep);
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

end Node;


package body Plunderer is

    task body PlundererTask is
        targetIndex: Natural;
        target: pNodeObj;
        n: Natural := nodes'Length;

        exitTask: Boolean := False;
    begin
        loop
            select
                accept Stop do
                    exitTask := True;
                end Stop;
            else
                SleepForSomeTime(maxSleep, intervals);

                -- pick a node
                targetIndex := RAD.Next(n);
                target := nodes(targetIndex);
                -- setup a trap
                target.all.nodeTask.all.SetupTrap;
            end select;
            if exitTask then
                exit;
            end if;
        end loop;
    end PlundererTask;

end Plunderer;

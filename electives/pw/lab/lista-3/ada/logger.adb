
package body Logger is

    task body LoggerReceiver is
        exitTask: Boolean := False;
    begin
        loop
            select
                accept Log(message: String) do
                    PrintBounded(message);
                end Log;
                or
                accept Stop do
                    -- allow for pending requests to be fulfilled
                    loop
                        select
                            accept Log(message: String) do
                                PrintBounded(message);
                            end Log;
                        or
                            delay 1.0;
                            exit;
                        end select;
                    end loop;
                    exitTask := True;
                end Stop;
            end select;
            if exitTask then
                exit;
            end if;
        end loop;
    end LoggerReceiver;

end Logger;

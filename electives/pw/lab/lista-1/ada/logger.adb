
package body Logger is

    task body LoggerReceiver is
        subtype RangeN is Natural range 1..n;
        subtype RangeNE is Natural range 0..(n-1);
        subtype RangeD is Natural range 1..d;
        subtype RangeK is Natural range 1..k;

        -- gather stats
        type NodeStats is array (RangeN, RangeK) of Boolean;
        type pNodeStats is access NodeStats;
        type MessageStats is array (RangeK, RangeN) of Boolean;
        type pMessageStats is access MessageStats;
        nodeSeen: pNodeStats := new NodeStats;
        messageVisited: pMessageStats := new MessageStats;

        exitTask: Boolean := False;
    begin
        loop
            select
                accept Log(message: string) do
                    PrintBounded(message);
                end Log;
                or
                accept LogMessageInTransit(msg: Natural; node: Natural) do
                    if msg in RangeK'Range and node in RangeNE'Range then
                        nodeSeen(node+1, msg) := True;
                        messageVisited(msg, node+1) := True;
                        PrintBounded("message" & Natural'Image(msg) & " has arrived at node" & Natural'Image(node));
                    end if;
                end LogMessageInTransit;
                or
                accept Stop do
                    PrintBounded("");
                    PrintBounded("Stats:");
                    for I in RangeK'Range loop
                        PrintBounded("message" & Natural'Image(I) & " visited:");
                        for J in RangeN'Range loop
                            if messageVisited(I, J) then
                                PrintBounded("  node" & Natural'Image(J-1));
                            end if;
                        end loop;
                    end loop;
                    PrintBounded("---");
                    for I in RangeN'Range loop
                        PrintBounded("node" & Natural'Image(I-1) & " seen:");
                        for J in RangeK'Range loop
                            if nodeSeen(I, J) then
                                PrintBounded("  message" & Natural'Image(J));
                            end if;
                        end loop;
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

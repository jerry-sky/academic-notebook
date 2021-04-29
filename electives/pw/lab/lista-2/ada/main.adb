with External; use External;
with Node; use Node;
with Ada.Containers.Doubly_Linked_Lists;
with Logger;
with RandInt;

procedure Main is

    package LST is new Ada.Containers.Doubly_Linked_Lists(Element_Type => pNodeObj);

    n: Natural;
    d: Natural;
    k: Natural;
    maxSleep: Natural;

begin
    if CMD.Argument_Count /= 4 then
        PrintBounded("four arguments necessary");
        return;
    end if;

    n := Natural'Value(CMD.Argument(1));
    d := Natural'Value(CMD.Argument(2));
    k := Natural'Value(CMD.Argument(3));
    maxSleep := Natural'Value(CMD.Argument(4));

    declare

        subtype RangeN is Natural range 1..n;
        nodes: pArray_pNodeObj;

        -- holder of `d` additional edges
        subtype RangeD is Natural range 1..d;
        -- RangeD (extended): `0` means there is no shortcut
        subtype RangeDE is Natural range 0..d;
        package RAD renames RandInt;
        type AdditionalEdges is array (RangeD, 1..2) of Natural;
        type pAdditionalEdges is access AdditionalEdges;
        shortcuts: pAdditionalEdges;

        type AdditionalEdgesArrayLengths is array (RangeN) of Natural;
        type pAdditionalEdgesArrayLengths is access AdditionalEdgesArrayLengths;
        shortcutsLengths: pAdditionalEdgesArrayLengths;

        subtype RangeK is Natural range 1..k;

        package LOG renames Logger;
        loggerReceiver: LOG.pLoggerReceiver;

        tmp: Natural := 0;
        tmp2: Natural := 0;
        tmp3: Natural := 0;

        tmpExit: Boolean := False;

        tmpNodeObj: pNodeObj;
        tmpNodeObj2: pNodeObj;

        tmpMessage: pMessage;

        task type SenderTask(firstNode: pNodeObj);
        task body SenderTask is
        begin
            for I in RangeK'Range loop
                tmpMessage := new Message'(content => I);
                firstNode.all.nodeTask.all.SendMessage(tmpMessage);
            end loop;
        end SenderTask;

        type pSenderTask is access SenderTask;

        sender: pSenderTask;

    begin

        -- instantiate the logger task
        loggerReceiver := new LOG.LoggerReceiver(n, d, k);

        -- create all nodes
        nodes := new Array_pNodeObj(RangeN);
        for I in RangeN'Range loop

            nodes.all(I) := new NodeObj;
            nodes.all(I).all.id := I-1;

        end loop;

        -- generate shortcuts
        shortcuts := new AdditionalEdges;
        for I in RangeD'Range loop
            tmp := RAD.Next(n);
            tmp2 := RAD.Next(n);
            if tmp > tmp2 then
                tmp3 := tmp;
                tmp := tmp2;
                tmp2 := tmp3;
            end if;
            if tmp /= tmp2 then
                -- shortcut successfully created
                shortcuts(I, 1) := tmp;
                shortcuts(I, 2) := tmp2;
                loggerReceiver.Log("shortcut" & Natural'Image(tmp-1) & " →" & Natural'Image(tmp2-1));
            else
                shortcuts(I, 1) := 0;
                shortcuts(I, 2) := 0;
            end if;
        end loop;

        loggerReceiver.Log("---");

        -- we need to precalculate the neighbours’ array size
        shortcutsLengths := new AdditionalEdgesArrayLengths;
        -- initialize with `1`, because each node has at least one neighbour
        for I in RangeN'Range loop
            shortcutsLengths.all(I) := 1;
        end loop;
        shortcutsLengths.all(RangeN'Last) := 0;
        -- count all the additional edges
        for I in RangeD'Range loop
            -- get the beginning node
            tmp := shortcuts(I, 1);
            if tmp > 0 and tmp <= n then
                shortcutsLengths.all(tmp) := shortcutsLengths.all(tmp) + 1;
            end if;
        end loop;
        -- special case for the last node

        -- now we can initialize our nodes
        for I in RangeN'Range loop
            tmpNodeObj := nodes.all(I);
            tmpNodeObj.all.neighbours := new Array_pNodeObj(1..shortcutsLengths.all(I));
            if I < n then
                tmpNodeObj.all.nodeTask := new NodeTask(tmpNodeObj, maxSleep, loggerReceiver, False);
            else
                tmpNodeObj.all.nodeTask := new NodeTask(tmpNodeObj, maxSleep, loggerReceiver, True);
            end if;
        end loop;
        -- and add pointers to neighbours
        for I in RangeD'Range loop
            -- get the beginning node of the edge
            tmp := shortcuts.all(I, 1);
            if tmp /= 0 then
                tmpNodeObj := nodes.all(tmp);
                -- get the ending node of the edge
                tmp2 := shortcuts.all(I, 2);
                tmpNodeObj2 := nodes.all(tmp2);
                -- add the neighbour (we’re using the lengths array as our pointer)
                tmpNodeObj.all.neighbours(shortcutsLengths.all(tmp)) := tmpNodeObj2;
                -- decrease the array pointer
                shortcutsLengths.all(tmp) := shortcutsLengths.all(tmp) - 1;
            end if;
        end loop;
        -- also add the edges for adjacent nodes
        for I in RangeN'Range loop
            -- current node
            tmpNodeObj := nodes(I);
            if I < n then
                -- next node
                tmpNodeObj2 := nodes(I+1);
                -- add as neighbour
                tmpNodeObj.all.neighbours(1) := tmpNodeObj2;
            else
                -- special case for the last node
                null;
            end if;
        end loop;

        -- send the messages
        tmpNodeObj2 := nodes(RangeN'First);
        sender := new SenderTask(tmpNodeObj2);

        -- receive the messages
        tmpNodeObj := nodes(RangeN'Last);
        for I in RangeK'Range loop
            tmpMessage := new Message;
            if tmpMessage /= null then
                tmpNodeObj.all.nodeTask.all.ReceiveMessage(tmpMessage);
                loggerReceiver.Log("→→→message" & Natural'Image(tmpMessage.all.content) & " received");
            end if;
        end loop;

        for I in RangeN'Range loop
            nodes(I).all.nodeTask.Stop;
        end loop;
        loggerReceiver.Stop;

    end;

end Main;

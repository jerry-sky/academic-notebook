with External; use External;
with Node; use Node;
with Logger;
with RandInt;
with Sender; use Sender;
with Receiver; use Receiver;
with EdgeRegistry; use EdgeRegistry;
with Plunderer; use Plunderer;

procedure Main is

    package EDG renames EdgeRegistry;

    n: Natural;
    d: Natural;
    b: Natural;
    k: Natural;
    h: Natural;
    maxSleep: Natural;
    plundererIntervals: Natural := 0;

begin
    if CMD.Argument_Count < 6 then
        PrintBounded("six arguments necessary");
        return;
    end if;

    n := Natural'Value(CMD.Argument(1));
    d := Natural'Value(CMD.Argument(2));
    b := Natural'Value(CMD.Argument(3));
    k := Natural'Value(CMD.Argument(4));
    h := Natural'Value(CMD.Argument(5));
    maxSleep := Natural'Value(CMD.Argument(6));

    if CMD.Argument_Count > 6 then
        plundererIntervals := Natural'Value(CMD.Argument(7));
    end if;

    -- first step of getting to the first node is free
    h := Natural'Succ(h);

    declare

        subtype RangeN is Natural range 1..n;
        subtype RangeD is Natural range 1..d;
        subtype RangeB is Natural range 1..b;
        subtype RangeK is Natural range 1..k;

        nodes: pArray_pNodeObj;

        package RAD renames RandInt;
        type AdditionalEdges is array (Natural range <>, Natural range <>) of Natural;
        type pAdditionalEdges is access AdditionalEdges;

        shortcuts: pAdditionalEdges;
        shortcutsEdgeRegistry: EDG.HashMap;

        detours: pAdditionalEdges;
        detoursEdgeRegistry: EDG.HashMap;

        type AdditionalEdgesArrayLengths is array (RangeN) of Natural;
        type pAdditionalEdgesArrayLengths is access AdditionalEdgesArrayLengths;
        neighboursLengths: pAdditionalEdgesArrayLengths;

        package LOG renames Logger;
        logger: LOG.pLoggerReceiver;

        tmp: Natural := 0;
        tmp2: Natural := 0;
        tmp3: Natural := 0;

        iter: Natural := 0;

        tmpExit: Boolean := False;

        tmpNodeObj: pNodeObj;
        tmpNodeObj2: pNodeObj;

        sender: pSenderTask;
        receiver: pReceiverTask;
        plunderer: pPlundererTask;

        reapers: pArray_pNodeTaskGrimReaper;

    begin

        -- instantiate the logger task
        logger := new LOG.LoggerReceiver(n, d, k);

        -- create all nodes
        nodes := new Array_pNodeObj(RangeN);
        for I in RangeN'Range loop
            nodes.all(I) := new NodeObj;
            nodes.all(I).all.id := Natural'Pred(I);
        end loop;

        -- generate shortcuts
        logger.Log("shortcuts:");
        shortcuts := new AdditionalEdges(RangeD, 1..2);
        iter := 1;
        while iter <= d loop
            tmp := RAD.Next(n);
            tmp2 := RAD.Next(n);
            if tmp > tmp2 then
                tmp3 := tmp;
                tmp := tmp2;
                tmp2 := tmp3;
            end if;
            if tmp /= tmp2 and not EDG.Exists(shortcutsEdgeRegistry, tmp, tmp2) then
                -- indexes are not equal, and the potential edge is
                -- not a duplicate of a one already existing
                shortcuts(iter, 1) := tmp;
                shortcuts(iter, 2) := tmp2;
                logger.Log(Natural'Image(tmp-1) & " →" & Natural'Image(tmp2-1));
                -- save the edge in the registry to avoid duplicates
                EDG.Register(shortcutsEdgeRegistry, tmp, tmp2);
                iter := Natural'Succ(iter); -- succulent
            end if;
        end loop;

        logger.Log("");

        -- generate detours
        logger.Log("detours:");
        detours := new AdditionalEdges(RangeB, 1..2);
        iter := 1;
        while iter <= b loop
            tmp := RAD.Next(n);
            tmp2 := RAD.Next(n);
            if tmp < tmp2 then
                tmp3 := tmp;
                tmp := tmp2;
                tmp2 := tmp3;
            end if;
            if tmp /= tmp2 and not EDG.Exists(detoursEdgeRegistry, tmp, tmp2) then
                -- indexes are not equal, and the potential edge is
                -- not a duplicate of a one already existing
                detours(iter, 1) := tmp;
                detours(iter, 2) := tmp2;
                logger.Log(Natural'Image(tmp-1) & " →" & Natural'Image(tmp2-1));
                -- save the edge in the registry to avoid duplicates
                EDG.Register(detoursEdgeRegistry, tmp, tmp2);
                iter := Natural'Succ(iter); -- succulent
            end if;
        end loop;

        logger.Log("");

        -- we need to precalculate the neighbours’ array size
        neighboursLengths := new AdditionalEdgesArrayLengths;
        -- initialize with `1`, because each node has at least one neighbour
        for I in RangeN'Range loop
            neighboursLengths.all(I) := 1;
        end loop;
        neighboursLengths.all(RangeN'Last) := 0;
        -- count all the additional edges
        for I in RangeD'Range loop
            -- get the beginning node
            tmp := shortcuts(I, 1);
            if tmp > 0 and tmp <= n then
                neighboursLengths.all(tmp) := neighboursLengths.all(tmp) + 1;
            end if;
        end loop;
        for I in RangeB'Range loop
            -- get the beginning node
            tmp := detours(I, 1);
            if tmp > 0 and tmp <= n then
                neighboursLengths.all(tmp) := neighboursLengths.all(tmp) + 1;
            end if;
        end loop;

        -- setup the receiver
        receiver := new ReceiverTask(k);

        -- now we can initialize our nodes
        for I in RangeN'Range loop
            tmpNodeObj := nodes.all(I);
            tmpNodeObj.all.neighbours := new Array_pNodeObj(1..neighboursLengths.all(I));
            if I < n then
                tmpNodeObj.all.nodeTask := new NodeTask(tmpNodeObj, maxSleep, logger, False, receiver);
            else
                tmpNodeObj.all.nodeTask := new NodeTask(tmpNodeObj, maxSleep, logger, True, receiver);
            end if;
        end loop;

        -- and add pointers to neighbours (shortcuts)
        for I in RangeD'Range loop
            -- get the beginning node of the edge
            tmp := shortcuts.all(I, 1);
            if tmp /= 0 then
                tmpNodeObj := nodes.all(tmp);
                -- get the ending node of the edge
                tmp2 := shortcuts.all(I, 2);
                tmpNodeObj2 := nodes.all(tmp2);
                -- add the neighbour (we’re using the lengths array as our pointer)
                tmpNodeObj.all.neighbours(neighboursLengths.all(tmp)) := tmpNodeObj2;
                -- decrease the array pointer
                neighboursLengths.all(tmp) := neighboursLengths.all(tmp) - 1;
            end if;
        end loop;

        -- and add pointers to neighbours (detours)
        for I in RangeB'Range loop
            -- get the beginning node of the edge
            tmp := detours.all(I, 1);
            if tmp /= 0 then
                tmpNodeObj := nodes.all(tmp);
                -- get the ending node of the edge
                tmp2 := detours.all(I, 2);
                tmpNodeObj2 := nodes.all(tmp2);
                -- add the neighbour (we’re using the lengths array as our pointer)
                tmpNodeObj.all.neighbours(neighboursLengths.all(tmp)) := tmpNodeObj2;
                -- decrease the array pointer
                neighboursLengths.all(tmp) := neighboursLengths.all(tmp) - 1;
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

        if plundererIntervals /= 0 then
            -- setup the plunderer
            logger.Log("plunderer active");
            logger.Log("");
            plunderer := new PlundererTask(nodes, maxSleep, plundererIntervals);
        end if;

        -- send the messages
        tmpNodeObj2 := nodes(RangeN'First);
        sender := new SenderTask(tmpNodeObj2, k, h);

        -- wait for the receiver
        receiver.all.Ended;

        -- employ a squadron of grim reapers that kill all node tasks
        reapers := new Array_pNodeTaskGrimReaper(RangeN);
        for I in RangeN'Range loop
            reapers(I) := new NodeTaskGrimReaper(nodes(I));
        end loop;
        logger.Stop;

    end;

end Main;

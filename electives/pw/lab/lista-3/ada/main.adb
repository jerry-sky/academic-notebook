with External; use External;
with Node; use Node;
with Logger;
with RandInt;
with EdgeRegistry; use EdgeRegistry;

procedure Main is

    package EDG renames EdgeRegistry;

    n: Natural;
    d: Natural;
    maxSleep: Natural;

begin
    if CMD.Argument_Count < 3 then
        PrintBounded("necessary arguments: n d maxSleep");
        return;
    end if;

    n := Natural'Value(CMD.Argument(1));
    d := Natural'Value(CMD.Argument(2));
    maxSleep := Natural'Value(CMD.Argument(3));

    declare

        subtype RangeN is Natural range 1..n;
        subtype RangeD is Natural range 1..d;

        nodes: Array_pNodeObj(RangeN);

        package RAD renames RandInt;
        type AdditionalEdges is array (Natural range <>, Natural range <>) of Natural;
        type pAdditionalEdges is access AdditionalEdges;

        shortcuts: pAdditionalEdges;
        shortcutsEdgeRegistry: EDG.HashMap;

        type AdditionalEdgesArrayLengths is array (RangeN) of Natural;
        type pAdditionalEdgesArrayLengths is access AdditionalEdgesArrayLengths;
        neighboursLengths: pAdditionalEdgesArrayLengths;

        package LOG renames Logger;
        logger: LOG.pLoggerReceiver;

        tmp: Natural := 0;
        tmp2: Natural := 0;
        tmp3: Natural := 0;
        tmpMString: MString := ToMString("");

        iter: Natural := 0;

        tmpExit: Boolean := False;

        tmpNodeObj: pNodeObj;
        tmpNodeObj2: pNodeObj;
        nextNode: pNodeObj;
        previousNode: pNodeObj;

        currentState: Natural := 0;

        reapers: Array_pNodeTaskGrimReaper(RangeN);

    begin

        -- instantiate the logger task
        logger := new LOG.LoggerReceiver;

        -- create all nodes
        for I in RangeN'Range loop
            nodes(I) := new NodeObj(n);
            nodes(I).all.id := I;
        end loop;

        -- generate shortcuts
        logger.Log("shortcuts:");
        shortcuts := new AdditionalEdges(RangeD, 1..2);
        iter := 1;
        while iter <= d loop
            tmp := RAD.Next(n);
            tmp2 := RAD.Next(n);
            if tmp /= tmp2 and not EDG.Exists(shortcutsEdgeRegistry, tmp, tmp2) then
                -- indexes are not equal, and the potential edge is
                -- not a duplicate of a one already existing

                -- save as a two-way edge
                shortcuts(iter, 1) := tmp;
                shortcuts(iter, 2) := tmp2;

                logger.Log(Natural'Image(tmp) & " →" & Natural'Image(tmp2));
                -- save the edge in the registry to avoid duplicates
                EDG.Register(shortcutsEdgeRegistry, tmp, tmp2);
                iter := Natural'Succ(iter); -- succulent
            end if;
        end loop;

        logger.Log("");

        -- we need to precalculate the neighbours’ array size
        neighboursLengths := new AdditionalEdgesArrayLengths;
        -- initialize with a `2`, because each node has two neighbours on the Hamilton path…
        for I in RangeN'Range loop
            neighboursLengths.all(I) := 2;
        end loop;
        -- …apart from the first and last nodes
        neighboursLengths.all(1) := 1;
        neighboursLengths.all(n) := 1;

        -- count all the additional edges
        for I in RangeD'Range loop
            -- get the beginning node
            tmp := shortcuts(I, 1);
            tmp2 := shortcuts(I, 2);
            if tmp >= 1 and tmp <= n and tmp2 >= 1 and tmp2 <= n then
                neighboursLengths.all(tmp) := neighboursLengths.all(tmp) + 1;
                neighboursLengths.all(tmp2) := neighboursLengths.all(tmp2) + 1;
            end if;
        end loop;

        -- now we can initialize our nodes
        for i in RangeN'Range loop
            tmpNodeObj := nodes(i);
            tmpNodeObj.all.neighbours := new Array_pNodeObj(1..neighboursLengths.all(i));
        end loop;

        -- and add pointers to neighbours
        for I in RangeD'Range loop
            -- get the beginning node of the edge
            tmp := shortcuts.all(I, 1);
            if tmp /= 0 then
                tmpNodeObj := nodes(tmp);
                -- get the ending node of the edge
                tmp2 := shortcuts.all(I, 2);
                tmpNodeObj2 := nodes(tmp2);
                -- add the neighbour (we’re using the lengths array as our pointer)
                tmpNodeObj.all.neighbours(neighboursLengths.all(tmp)) := tmpNodeObj2;
                -- decrease the array pointer
                neighboursLengths.all(tmp) := neighboursLengths.all(tmp) - 1;
                -- (two-way)
                tmpNodeObj2.all.neighbours(neighboursLengths.all(tmp2)) := tmpNodeObj;
                neighboursLengths.all(tmp2) := neighboursLengths.all(tmp2) - 1;
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
                tmpNodeObj.all.neighbours(neighboursLengths.all(I)) := tmpNodeObj2;
                neighboursLengths.all(I) := neighboursLengths.all(I)-1;
                tmpNodeObj2.all.neighbours(neighboursLengths.all(I+1)) := tmpNodeObj;
                neighboursLengths.all(I+1) := neighboursLengths.all(I+1)-1;
            end if;
        end loop;

        -- generate routing information based only on the main Hamilton path
        -- consisting of edges {v, v+1}
        for i in RangeN'Range loop
            tmpNodeObj := nodes(i);

            previousNode := null;
            if i > 1 then
                previousNode := nodes(i-1);
            end if;
            nextNode := null;
            if i < n then
                nextNode := nodes(i+1);
            end if;

            for j in RangeN'Range loop
                if j = i then
                    tmpNodeObj.all.routing.changed(j) := False;
                else
                    tmpNodeObj.all.routing.changed(j) := True;
                    tmpNodeObj.all.routing.cost(j) := abs (i-j);
                    if i < j then
                        tmpNodeObj.all.routing.nextHop(j) := nextNode;
                    else -- i > j
                        tmpNodeObj.all.routing.nextHop(j) := previousNode;
                    end if;
                end if;
            end loop;
        end loop;

        -- generate routing information for the direct neighbours
        for i in RangeN'Range loop
            tmpNodeObj := nodes(i);

            for j in tmpNodeObj.all.neighbours.all'Range loop
                tmpNodeObj2 := tmpNodeObj.all.neighbours.all(j);
                tmp := tmpNodeObj2.all.id;
                tmpNodeObj.all.routing.cost(tmp) := 1;
                tmpNodeObj.all.routing.nextHop(tmp) := tmpNodeObj2;
            end loop;
        end loop;

        -- run all necessary tasks on all nodes
        for i in RangeN'Range loop
            tmpNodeObj := nodes(i);

            tmpNodeObj.all.stash := new NodeStash(tmpNodeObj, logger);
            tmpNodeObj.all.senderTask := new SenderTask(tmpNodeObj, n, maxSleep, logger);
            tmpNodeObj.all.receiverTask := new ReceiverTask(tmpNodeObj, n, logger);
        end loop;

        -- wait for all nodes to fully discover the network topology
        loop
            SleepForSomeTime(maxSleep);

            currentState := 0;
            for i in nodes'Range loop
                tmpNodeObj := nodes(i);
                for j in tmpNodeObj.all.routing.changed'Range loop
                    if i /= j and tmpNodeObj.all.routing.changed(j) then
                        currentState := Natural'Succ(currentState); -- succulent
                    end if;
                end loop;
            end loop;

            if currentState = 0 then
                exit;
            end if;
        end loop;

        -- employ a squadron of grim reapers that kill all node tasks
        for I in RangeN'Range loop
            reapers(I) := new NodeTaskGrimReaper(nodes(I), logger);
        end loop;

        -- print routing tables for all nodes
        logger.Log("");
        logger.Log("routing tables for all nodes");
        logger.Log("format: ‘next hop node id’ → ‘destination node id’ (cost)");
        logger.Log("    or: ‘next hop node id’ direct // for direct neighbours");
        logger.Log("");
        for i in RangeN'Range loop
            tmpNodeObj := nodes(i);
            logger.Log("node" & Natural'Image(tmpNodeObj.all.id) & " — routing table:");

            for j in RangeN'Range loop
                if j /= tmpNodeObj.all.id then
                    tmp := tmpNodeObj.all.routing.nexthop(j).id;
                    if tmp /= j then
                        tmpMString := ToMString(Natural'Image(tmpNodeObj.all.routing.cost(j)));
                        tmpMString := DeleteLeftCharacters(tmpMString, 1, 1);
                        logger.Log(" " & Natural'Image(tmp) & " →" & Natural'Image(j) & " (" & ToString(tmpMString) & ")");
                    else
                        logger.Log(" " & Natural'Image(tmp) & " direct");
                    end if;
                end if;
            end loop;

            logger.Log("");
        end loop;

        logger.Stop;
    end;

end Main;

with RandInt;
with Logger; use Logger;
with External; use External;

package Node is

    package RAD renames RandInt;

    type NodeObj;

    type pNodeObj is access NodeObj;

    type Array_pNodeObj is array (Natural range <>) of pNodeObj;
    type pArray_pNodeObj is access Array_pNodeObj;

    type Offer is record
        id: Natural;
        currentCost: Natural;
    end record;

    type pOffer is access Offer;
    type Array_pOffer is array (Natural range <>) of pOffer;
    type pArray_pOffer is access Array_pOffer;

    type Message is record
        contents: pArray_pOffer;
        sender: pNodeObj;
    end record;

    type pMessage is access Message;

    task type ReceiverTask(self: pNodeObj; n: Natural; logger: pLoggerReceiver) is
        entry GetMessage(tmpMessage: pMessage);
        entry Stop;
    end ReceiverTask;

    type pReceiverTask is access ReceiverTask;

    task type SenderTask(self: pNodeObj; n: Natural; maxSleep: Natural; logger: pLoggerReceiver) is
        entry Stop;
    end SenderTask;

    type pSenderTask is access SenderTask;

    -- NodeStash simulates what a `chan` in Golang would do
    task type NodeStash(self: pNodeObj; logger: pLoggerReceiver) is
        entry SendMessage(message: pMessage);
        entry Stop;
    end NodeStash;

    type pNodeStash is access NodeStash;

    type ArrayNatural is array (Natural range <>) of Natural;
    type ArrayBoolean is array (Natural range <>) of Boolean;
    type RoutingTable(n: Natural) is record
        cost: ArrayNatural(1..n);
        nextHop: Array_pNodeObj(1..n);
        changed: ArrayBoolean(1..n);
    end record;

    type NodeObj(n: Natural) is record
        id: Natural;
        neighbours: pArray_pNodeObj;
        stash: pNodeStash;
        routing: RoutingTable(n);
        senderTask: pSenderTask;
        receiverTask: pReceiverTask;
    end record;

    -- grim reaper kills given node
    task type NodeTaskGrimReaper(node: pNodeObj; logger: pLoggerReceiver);

    type pNodeTaskGrimReaper is access NodeTaskGrimReaper;
    type Array_pNodeTaskGrimReaper is array (Positive range <>) of pNodeTaskGrimReaper;
    type pArray_pNodeTaskGrimReaper is access Array_pNodeTaskGrimReaper;

end Node;

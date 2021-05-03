with Ada.Numerics.Float_Random;
with RandInt;
with Logger;
with External; use External;
with Receiver;

package Node is

    package RAF renames Ada.Numerics.Float_Random;
    package LOG renames Logger;
    package RAD renames RandInt;
    package REC renames Receiver;

    type NodeObj;

    type pNodeObj is access NodeObj;

    type Array_pNodeObj is array (Positive range <>) of pNodeObj;
    type pArray_pNodeObj is access Array_pNodeObj;

    type Message is record
        content: Natural;
        health: Natural;
    end record;

    type pMessage is access Message;

    procedure SleepForSomeTime(maxSleep: Natural; intervals: Natural := 1);

    task type NodeTask(
        self: pNodeObj;
        maxSleep: Natural;
        logger: LOG.pLoggerReceiver;
        isLast: Boolean;
        receiver: REC.pReceiverTask
    ) is
        entry SendMessage(message: in pMessage);
        entry SetupTrap;
        entry Stop;
    end NodeTask;

    type pNodeTask is access NodeTask;

    -- NodeStash sort of simulates what a `chan` in Golang would do
    task type NodeStash(
        self: pNodeObj
    ) is
        entry SendMessage(message: in pMessage);
        entry Stop;
    end NodeStash;

    type pNodeStash is access NodeStash;

    type NodeObj is record
        id: Natural;
        neighbours: pArray_pNodeObj;
        nodeTask: pNodeTask;
        nodeStash: pNodeStash;
    end record;

    -- grim reaper kills given node
    task type NodeTaskGrimReaper(node: pNodeObj);

    type pNodeTaskGrimReaper is access NodeTaskGrimReaper;
    type Array_pNodeTaskGrimReaper is array (Positive range <>) of pNodeTaskGrimReaper;
    type pArray_pNodeTaskGrimReaper is access Array_pNodeTaskGrimReaper;

end Node;

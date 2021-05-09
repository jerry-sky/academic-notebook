with Node; use Node;
with RandInt;

package Plunderer is

    package RAD renames RandInt;

    task type PlundererTask(nodes: pArray_pNodeObj; maxSleep: Natural; intervals: Natural) is
        entry Stop;
    end PlundererTask;

    type pPlundererTask is access PlundererTask;

end Plunderer;

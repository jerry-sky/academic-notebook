with Ada.Containers.Ordered_Maps;
with Ada.Strings.Unbounded;
with External; use External;

package EdgeRegistry is

    package HMP is new Ada.Containers.Ordered_Maps(
        Key_Type => MString,
        Element_Type => Boolean,
        "<" => Ada.Strings.Unbounded."<"
    );

    subtype HashMap is HMP.Map;

    procedure Register(map: in out HashMap; a: Natural; b: Natural);
    function Exists(map: HashMap; a: Natural; b: Natural) return Boolean;

    private
        function Key(a: Natural; b: Natural) return MString;

end EdgeRegistry;

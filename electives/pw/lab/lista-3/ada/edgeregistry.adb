
package body EdgeRegistry is

    function Key(a: Natural; b: Natural) return MString is
    begin
        return ToMString(Natural'Image(a) & ";" & Natural'Image(b));
    end Key;

    procedure Register(map: in out HashMap; a: Natural; b: Natural) is
    begin
        map.Insert(Key(a, b), True);
        map.Insert(Key(b, a), True);
    end Register;

    function Exists(map: HashMap; a: Natural; b: Natural) return Boolean is
    begin
        return map.Contains(Key(a, b));
    end Exists;

end EdgeRegistry;

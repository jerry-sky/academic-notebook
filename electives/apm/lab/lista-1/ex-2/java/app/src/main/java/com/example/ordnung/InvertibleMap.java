package com.example.ordnung;

import java.util.HashMap;
import java.util.function.BiConsumer;

public class InvertibleMap<T, S> {
    private HashMap<T, S> primary = new HashMap<>();
    private HashMap<S, T> inverted = new HashMap<>();

    public InvertibleMap(HashMap<T, S> first) {
        first.forEach(
            (t, s) -> {
                this.primary.put(t, s);
                this.inverted.put(s, t);
            }
        );
    }

    public S getObj(T key) {
        return this.primary.get(key);
    }

    public T getKey(S obj) {
        return this.inverted.get(obj);
    }

    public void forEach(BiConsumer<T, S> action) {
        this.primary.forEach(action);
    }

    public int size() {
        return this.primary.size();
    }

}

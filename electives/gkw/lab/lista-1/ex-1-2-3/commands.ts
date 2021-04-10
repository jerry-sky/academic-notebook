
export enum CommandToken {
    FORWARD = 'F',
    BACKWARD = 'B',
    LEFT = 'L',
    RIGHT = 'R',
    REPEAT = 'RE',
    PROCEDURE_BEGIN = 'BE',
    BRACKET_OPEN = '[',
    BRACKET_CLOSE = ']',
    PROCEDURE_END = 'EN',
    PROCEDURE_TERMINATE = 'TE',
    IF = 'IF',
    CALC = 'CA',
    EQUALS = '='
}

export namespace CommandToken {

    const allValues: string[] = Object.keys(CommandToken).map((key) => CommandToken[key])

    export function isOfType(val: any): val is CommandToken {
        if (allValues.indexOf(val) !== -1) {
            return true
        }
        return false
    }
}

export enum MathOperator {
    DIVIDE = '/',
    SUBTRACT = '-',
    ADD = '+',
    MULTIPLY = '*'
}

export namespace MathOperator {

    const allValues: string[] = Object.keys(MathOperator).map((key) => MathOperator[key])

    export function isOfType(val: any): val is MathOperator {
        if (allValues.indexOf(val) !== -1) {
            return true
        }
        return false
    }
}

export type RepeatReturnToken = {
    /**
     * How many more times the block needs to be run.
     */
    repeat: number,
    /**
     * Where does the repeat block begin.
     */
    index: number
}

export type TokenStackElement = string
    | CommandToken
    | RepeatReturnToken

export class CommandStack {

    public pointer: number = 0
    public stack: TokenStackElement[]

    constructor(stack?: string);
    constructor(stack: string) {
        if (stack) {
            // split given string of commands because of:
            // - whitespace,
            // - two tokens where one is the BRACKET token
            this.stack = stack.trim().split(/\s|(?<=\[)|(?=\])/)
        }
    }

    /**
     * Alternative constructor that skips the token parsing process.
     */
    public static from(stack: TokenStackElement[]): CommandStack {
        const commandStack = new CommandStack()
        commandStack.stack = stack
        return commandStack
    }

    public static copy(stack: CommandStack): CommandStack {
        const commandStack = new CommandStack()
        commandStack.stack = [...stack.stack]
        return commandStack
    }

    public get isDone(): boolean {
        return this.pointer > this.stack.length - 1
    }

    public get currentElement() {
        return this.stack[this.pointer]
    }

    public set currentElement(val: TokenStackElement) {
        this.stack[this.pointer] = val
    }

    /**
     * Get the next item of the stack without removing it.
     */
    public pop(): TokenStackElement {
        return this.stack[this.pointer++]
    }

    public popUntil(until: TokenStackElement): TokenStackElement[] {
        const output: TokenStackElement[] = []
        let i = this.pointer
        while (i < this.stack.length && this.stack[i] !== until) {
            output.push(this.stack[i])
            i++
        }
        this.pointer = i
        return output
    }

    /**
     * Pop `count` elements.
     */
    public popCount(count: number, hard: boolean = false): TokenStackElement[] {
        let output: TokenStackElement[]
        if (hard) {
            output = this.stack.splice(this.pointer, count)
        } else {
            output = this.stack.slice(this.pointer, this.pointer + count)
            this.pointer += count
        }
        return output
    }

    public putBack(elements: TokenStackElement[]) {
        this.stack.splice(this.pointer, 0, ...elements)
    }

    public insert(element: TokenStackElement, index: number = this.pointer) {
        this.stack.splice(index, 0, element)
    }

    public removePrevious() {
        this.stack.splice(this.pointer - 1, 1)
    }

    public terminate() {
        this.pointer = this.stack.length
    }

    public reset() {
        this.pointer = 0
    }

}

export class LogoProcedure {

    constructor(
        private _stack: CommandStack,
        private _args: string[]
    ) { }

    public get stack() {
        return this._stack
    }

    public get args() {
        return this._args
    }

    public get argCount() {
        return this._args.length
    }

}

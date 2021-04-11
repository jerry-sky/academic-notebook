import { MyCanvas } from './my-canvas'
import { CommandStack, CommandToken, LogoProcedure, MathOperator, RepeatReturnToken, TokenStackElement } from './commands'

// shorthand for parsing decimal numbers
const parseDecimal = (val: string) => parseInt(val, 10)

/**
 * The Logo command interpreter.
 */
export class LogoInterpreter {

    private tokenStack: CommandStack

    private procedures: {
        [key: string]: LogoProcedure
    } = {}

    constructor(
        private myCanvas: MyCanvas
    ) { }

    private handleAtomicAction(action: CommandToken, rawValue: string) {
        const value = parseDecimal(rawValue)
        switch (action) {
            case CommandToken.FORWARD:
                this.myCanvas.move(value)
                break
            case CommandToken.BACKWARD:
                this.myCanvas.move(-1 * value)
                break
            case CommandToken.LEFT:
                this.myCanvas.rotateXY(value)
                break
            case CommandToken.RIGHT:
                this.myCanvas.rotateXY(-1 * value)
                break
            case CommandToken.UPWARDS:
                this.myCanvas.rotateYZ(value)
                break
            case CommandToken.DOWNWARDS:
                this.myCanvas.rotateYZ(-1 * value)
                break
        }

    }

    public async ExecuteCommandStack(stack: string) {
        this.tokenStack = new CommandStack(stack)

        this.preComputeMathExpressions(this.tokenStack)

        while (!this.tokenStack.isDone) {
            await this.handleCommand()
        }

    }

    private findEndingBracket(openingBracketIndex: number, stack: CommandStack): number {
        let innerLoops = 0
        const s = stack.stack
        for (let i = openingBracketIndex + 1; i < s.length; i++) {
            if (s[i] === CommandToken.BRACKET_OPEN) {
                innerLoops++
            }
            else if (s[i] === CommandToken.BRACKET_CLOSE) {
                if (innerLoops == 0) {
                    // replace the ending bracket with a return packet
                    return i
                }
                else innerLoops--
            }
        }
    }

    /**
     * Compute the condition based on given operator token.
     */
    private computeCondition(elements: TokenStackElement[]): boolean {
        const left = elements[0]
        const operator = elements[1] as CommandToken
        const right = elements[2]
        switch (operator) {
            case CommandToken.EQUALS:
                if (left === right) {
                    return true
                } else {
                    return false
                }
        }

        return false
    }

    private computeExpression(elements: TokenStackElement[]): number {
        const left = parseDecimal(elements[0] as string)
        const operator = elements[1] as MathOperator
        const right = parseDecimal(elements[2] as string)
        switch (operator) {
            case MathOperator.DIVIDE:
                return left / right
            case MathOperator.ADD:
                return left + right
            case MathOperator.MULTIPLY:
                return left * right
            case MathOperator.SUBTRACT:
                return left - right
        }
    }

    private preComputeMathExpressions(stack: CommandStack) {

        while (!stack.isDone) {
            const e = stack.pop()
            if (e === CommandToken.CALC) {
                // we need three arguments
                // remove them, so they can be replaced by the expression result
                const elements = stack.popCount(3, true)
                // compute
                const result = this.computeExpression(elements)
                if (isNaN(result)) {
                    // the expression contained a variable that wasn’t replaced by its value yet
                    // we need to put back the original expression elements
                    stack.putBack(elements)
                } else {
                    // insert the result back into place of the expression
                    stack.insert(String(result))
                    // remove the CALC token
                    stack.removePrevious()
                }
            }
        }

        stack.reset()
    }

    /**
     * Handle given command.
     */
    private async handleCommand(stack = this.tokenStack) {

        // take the top token
        const actionToken = stack.pop()

        if (!actionToken) return

        if (CommandToken.isOfType(actionToken)) {
            // handle the token
            switch (actionToken) {
                case CommandToken.BACKWARD:
                case CommandToken.FORWARD:
                case CommandToken.LEFT:
                case CommandToken.RIGHT:
                case CommandToken.UPWARDS:
                case CommandToken.DOWNWARDS:
                    // expecting an action that takes exactly one argument
                    const value = stack.pop()
                    if (typeof value === 'string')
                        this.handleAtomicAction(actionToken, value)
                    break
                case CommandToken.REPEAT:
                    // how many times does the routine run
                    const timesRaw = stack.pop()
                    if (typeof timesRaw === 'string') {
                        const repeat = parseDecimal(timesRaw) - 1
                        // get the index of the next command
                        // that will be the first operation of the REPEAT clause
                        const index = stack.pointer
                        // place the return packet in place of the ending bracket
                        stack.stack[this.findEndingBracket(index, stack)] = {
                            index,
                            repeat
                        }
                    }
                    break
                case CommandToken.IF: {
                    // every token that is between IF and BRACKET_OPEN is the condition
                    const conditionElements = stack.popUntil(CommandToken.BRACKET_OPEN)
                    // we’re expecting three elements
                    const result = this.computeCondition(conditionElements)
                    if (result) {
                        // the condition is met, remove the opening bracket
                        stack.pop()
                    } else {
                        // otherwise skip the whole block
                        stack.popUntil(CommandToken.BRACKET_CLOSE)
                        // remove the closing bracket just in case
                        stack.pop()
                    }
                    break
                }
                case CommandToken.PROCEDURE_BEGIN: {
                    // get the name of the procedure
                    const name = stack.pop() as string
                    // get the count of the arguments
                    const argCount = parseDecimal(stack.pop() as string)
                    // get the arguments of the procedure
                    const args = stack.popCount(argCount) as string[]
                    // get all the commands of the procedure
                    const procedureInnerStack = stack.popUntil(CommandToken.PROCEDURE_END)
                    const procedure = new LogoProcedure(
                        CommandStack.from(procedureInnerStack),
                        args
                    )
                    // save the procedure
                    this.procedures[name] = procedure
                    break
                }
                case CommandToken.PROCEDURE_TERMINATE: {
                    // terminate the current stack
                    stack.terminate()
                    break
                }
            }
        } else if (Object.keys(this.procedures).includes(actionToken as string)) {
            // procedure

            const procedure = this.procedures[actionToken as string]
            // get args
            const argValues = stack.popCount(procedure.argCount) as string[]

            // copy the stack
            const innerStack = CommandStack.copy(procedure.stack)

            // replace arg names with values
            let i = 0
            innerStack.stack.forEach((element) => {
                if (procedure.args.includes(element as string)) {
                    const index = procedure.args.indexOf(element as string)
                    innerStack.stack[i] = argValues[index]
                }
                i++
            })

            this.preComputeMathExpressions(innerStack)

            // run the procedure
            while (!innerStack.isDone) {
                await this.handleCommand(innerStack)
            }

        } else if (typeof actionToken !== 'string') {
            // repeat return token

            if (actionToken.repeat > 0) {
                stack.pointer = actionToken.index
                actionToken.repeat--
            } else {
                stack.pointer--
                stack.currentElement = CommandToken.BRACKET_CLOSE
                stack.pointer++
            }

        }
    }

}

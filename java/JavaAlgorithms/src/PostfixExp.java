import java.util.Stack;

/**
 * This class evaluates a postfix expression.
 */
public class PostfixExp {
    /**
     * The main method of the program.
     * It demonstrates the usage of the evaluatePostfix method.
     *
     * @param args The command-line arguments.
     */
    public static void main(String[] args) {
        // postfix expression: 23*54*+9-
        String exp = "23*54*+9-";
        System.out.println("Postfix Expression: " + exp);
        System.out.println("Result: " + evaluatePostfix(exp));

        // infix expression: 10 + 5 * 6 + (9 * 3 + 8) * 2
        String infixExp = "1+5*6+(9*3+8)*2";
        System.out.println("Infix Expression: " + infixExp);
        String newExp = convertInfixToPostfix(infixExp);
        System.out.println("Postfix Expression: " + newExp);
        System.out.println("Result: " + evaluatePostfix(newExp));
    }
        

    /**
     * Evaluates a postfix expression and returns the result.
     *
     * @param exp The postfix expression to evaluate.
     * @return The result of the evaluation.
     */
    public static int evaluatePostfix(String exp){
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < exp.length(); i++){
            char c = exp.charAt(i);
            if(Character.isDigit(c)){
                // By subtracting the character '0' from c, we effectively 
                // convert the character digit into its corresponding integer 
                // value. For example, if c is the character '5', then c - '0' 
                // would evaluate to the integer value 5.
                stack.push(c - '0');
            } else {
                int val1 = stack.pop();
                int val2 = stack.pop();
                switch(c){
                    case '+':
                        stack.push(val2 + val1);
                        break;
                    case '-':
                        stack.push(val2 - val1);
                        break;
                    case '*':
                        stack.push(val2 * val1);
                        break;
                    case '/':
                        stack.push(val2 / val1);
                        break;
                }
            }
        }
        return stack.pop();
    }

    

    /**
     * Converts an infix expression to a postfix expression.
     *
     * @param exp The infix expression to convert.
     * @return The postfix expression.
     */
    public static String convertInfixToPostfix(String exp) {
        StringBuilder postfixExp = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < exp.length(); i++) {
            char c = exp.charAt(i);

            if (Character.isDigit(c)) {
                postfixExp.append(c);
            } else if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                // Pop and append all operators from the stack until a '(' is encountered.
                while (!stack.isEmpty() && stack.peek() != '(') {
                    postfixExp.append(stack.pop());
                }
                stack.pop(); // Discard the '('
            } else {
                // Pop and append all operators from the stack with higher or 
                // equal precedence.
                while (!stack.isEmpty() && precedence(c) <= precedence(stack.peek())) {
                    postfixExp.append(stack.pop());
                }
                stack.push(c);
            }
        }

        while (!stack.isEmpty()) {
            postfixExp.append(stack.pop());
        }

        return postfixExp.toString();
    }

    /**
     * Returns the precedence of an operator.
     *
     * @param operator The operator.
     * @return The precedence value.
     */
    private static int precedence(char operator) {
        switch (operator) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            default:
                return 0;
        }
    }




    


}

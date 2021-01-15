//***************Akahs Kumar*************************

class Solution {
    public String removeDuplicates(String S) {
        Stack<Character> stack = new Stack<>();

		for (int i = 0; i < S.length(); i++) {
			char ch = S.charAt(i);

			if (!stack.isEmpty() && stack.peek() == ch) {
				stack.pop();
			} else {
				stack.push(ch);
			}
		}

		StringBuffer result = new StringBuffer();
		while (!stack.isEmpty()) {
			result.append(stack.pop());
		}

		return result.reverse().toString();
    }
}

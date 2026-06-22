# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I played the game for the first time, I noticed a couple of bugs hints 
  1. Hints were opposite of what they should be
  2. Initial game only gives 7 tries, but future games give 8
  3. Doesn't actually start a new game; I'm trying to guess, but it's not registering as an attempt. You need to reload the whole game to actually play.
  4. Guessing a number not in [1, 100] still counts as an attempt

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| A guess of 50 | Output of "Go HIGHER" | Output of "GO LOWER" | Program still runs, just that logic fails |
| When "New Game" is clicked | "Attempts left: 7" | "Attempts left: 8" | Program essentially adds an extra attempt to the guessing game after the first game (no consistency) |
| A guess of -1 | Output of "INVALID INPUT" | Output of "Go LOWER" | Program should throw an error but doesn't and continues running |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used the Claude Code for VS Code Extension for this project. It was really helpful in fixing a lot of the bugs I found. 

For example, when I wanted to fix the "Opposite Hint" bug, Claude provided this: "The branches are swapped: when guess > secret it returns 'Go HIGHER!' (should be LOWER), and the else returns 'Go LOWER!' (should be HIGHER)." This suggestion was detailed as well as concise, enabling me to easily fix the bug.

To be honest, Claude did not provide any misleading/incorrect information; however, I was a bit confused while trying to fix the second bug because I fixed the code for the first bug before flagging the lines of the second bug. As a result, the line numbers Claude provided (since I asked for the suggestions at once, not one bug at a time) did not match the "actual" line numbers of the buggy code. So, I had to scan the code and use Claude's descriptions of the buggy lines to fix the second bug. It took more time than I wanted it to, but in the end, I was able to get through it utilizing my Python knowledge.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

A bug counted as fixed only when I could reproduce the original broken behavior and then see it gone in both the running app and an automated test. For the backwards-hint bug, I wanted a test that would fail on the old swapped logic; for the out-of-range bug, I checked not just that an invalid guess was rejected but that it no longer used up an attempt.

I ran pytest tests/test_game_logic.py. The test test_too_high_hint_says_go_lower calls check_guess(60, 50) and asserts the message says "LOWER," which confirmed the hint direction was finally correct. Running the suite also revealed that three starter tests compared the (outcome, message) tuple to a plain string, so they had never actually passed. I fixed them to unpack the tuple and ended at 9/9 passing.

AI helped me design tests that targeted the two bugs directly, including boundary cases I might have skipped (1 and 100 valid, -1 and 101 rejected). It also explained why the starter tests were failing instead of just telling me to change them, which helped me trust the fix.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you click a button or type something, Streamlit re-runs the whole script from top to bottom, which means normal variables reset each time. 

To remember things like the secret number, attempts, and score, you have to store them in st.session_state, which survives those reruns. Working on this game made it clear that "state" is just anything you need to outlive a single rerun.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

The habit I want to carry forward is testing a fix before believing it, writing a check that fails on the broken version first so a passing result actually means something instead of just looking right. 

Next time, I'd tackle bugs one at a time with the AI rather than asking about all of them at once, since fixing the first bug shifted everything below it and the guidance for the later bugs no longer lined up. 

This project made me see that AI-generated code should be used as a confident first draft rather than a finished answer. I'll need to verify it before trusting it.

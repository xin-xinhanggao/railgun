Please design test cases for a vending machine's software. In order to simplify the problem, we assume that all kinds of drinks in this vending machine costs $0.5. The usage rule of the vending machine is listed below.

*     Only $1 coins and $0.5 coins can be accepted.
*     Only sell orange juice and bear.
*     If the vending machine does not have change, the red light means "No Change" will be on.
  *   When the red light is on, if you put $1 coin into the vending machine and press down the drinks button, the machine will return your coin back .
 *    When the red light is off, if you put $1 coin into the vending machine and press down the drinks button,the machine will return you the change and corresponding drinks.

Please design test cases based on Cause Effect Graphing. The causes of the Cause Effect Graphing is listed below:

*   Whether the vending machine have change.
*   Whether the user puts into $1 coin.
*   Whether the user puts into $0.5 coin.
*   Whether the user presses down the "orange juice" button.
*   Whether the user presses down the "bear" button.

Owing to Cause 2 is mutual exclusive to Cause 3 and Cause 4 is mutual exclusive to Cause 5, we can use two variables to represent these 4 causes.

Please give the legal test cases( The case that user does nothing is not needed.)

In final test cases, we use variable <code> a</code> to express whether the vending machine has change(0 means no change,1 means that the vending machine has change). variable <code>b</code>expressing  the coin put into the machine( 0 means no coin is put into the machine , 1 means that users put into $0.5 coin, 2 means that users put into $1 coin).
variable <code>c </code> expressing the drink button's state(0 means the user does not press down the button, 1means that the users press down the "orange juice" button,2 means that the users press down the "bear" button ).

Please hand in your test cases in given text box. The test cases should be represented in CSV, and should contain CSV header <code>a,b,c</code>, for example:

    a,b,c
    1,2,1(means that the user put into $1 coin and press down the "orange juice" button when the vending machine has change )

Please upload your submission before deadline.
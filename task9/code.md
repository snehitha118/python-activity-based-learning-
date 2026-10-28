String-Based Examination

Answer Evaluation Using Python

1. Problem Statement

The aim of this activity is to develop a Python program to evaluate students' examination answers by comparing them with a predefined answer key. The program calculates the number of correct, incorrect, and unanswered questions, applies negative marking for incorrect answers, and displays the final score.

2.Algorithm:

1. Start the program.
2. Store the correct answers in an answer key list.
3. Get the student's answers as input.
4. Initialize the counters for correct, incorrect, and unanswered questions to zero.
5. Compare each student's answer with the corresponding answer in the answer key.
6. If the answer is correct, increase the correct-answer count.
7. If the answer is incorrect, increase the incorrect-answer count and apply negative marking.
8. If the answer is blank, increase the unanswered count.
9. Calculate the final score by subtracting the negative marks from the marks obtained for correct answers.
10. Display the correct, incorrect, and unanswered counts and the final score.
11. Stop the program.

3.Flowchart:
    
    A([Start]) --> B[/Input total classes, attended classes, required percentage/]
    
    B --> C[Calculate current attendance percentage]
    
    C --> D[Display current attendance]
    
    D --> E{Current percentage >= required percentage?}
    
    E -- Yes --> F[Display requirement met]
    
    F --> G[Display additional classes = 0]
    
    G --> M([End])
    
    E -- No --> H[Set additional classes = 0]
    
    H --> I{Current percentage < required percentage?}
    
    I -- Yes --> J[Increment additional classes]
    
    J --> K[Increment total and attended classes]
    
    K --> L[Recalculate current percentage]
    
    L --> I
    
    I -- No --> N[Display additional classes required]
    
    N --> O[Display updated attendance]
    
    O --> M
    

    4.Sample input:

    Enter total classes conducted: 100
    
Enter classes attended: 60

Enter required attendance percentage: 75

5.Sample output:

Current Attendance: 60.0 %

Attendance requirement can be met

Additional classes required: 60

Updated Attendance: 75.0 %








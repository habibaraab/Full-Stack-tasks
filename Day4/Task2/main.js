  let sum = 0;

        while (true) {
            let userInput = prompt("Enter a number:");
            let number = Number(userInput);
            if (userInput === null || number === 0) {
                break;
            }
            
            if (isNaN(number)) {
                alert("Invalid input. Please enter a valid number.");
                continue; 
            }

            sum += number;
            if (sum > 100) {
                alert("The sum has exceeded 100, stopping.");
                break; 
            }
        }

        document.writeln("<h3>The total sum is: " + sum + "</h3>");

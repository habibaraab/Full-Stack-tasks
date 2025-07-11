 const userInput = prompt("Please enter a sentence:");
        let c = 0;
        if (userInput) {
            for (let i = 0; i < userInput.length; i++) {
            
                if (userInput[i].toLowerCase() === 'e') {
                    c++;
                }
            }
            

            document.writeln("<h2>The number of 'e' characters is: " + c + "</h2>");

        }
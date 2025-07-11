  const input = prompt("Please enter a string to check if it's a palindrome:");

        if (input) {
          
            const ch = confirm("Check be case-sensitive?\n\n(OK = Yes, Cancel = No)");

            let chString = input;
            if (!ch) {
                chString = input.toLowerCase();
            }

            const reversedString = chString.split('').reverse().join('');

            let ans;
            if (chString === reversedString) {
                ans = `"${input}" is a palindrome.`;
            } else {
                ans = `"${input}" is NOT a palindrome.`;
            }
            
                    document.writeln(`<h2>${ans}</h2>`);

        }
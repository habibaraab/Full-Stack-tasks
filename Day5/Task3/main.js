const arr = [];
        for (let i = 0; i < 5; i++) {
            let num;

            while (true) {
                let userInput = prompt(`Enter  number ${i + 1} of 5:`);
    
                if (userInput === null) {
                    break;
                }

                num = Number(userInput);
                if (!isNaN(num)) {
                    break;
                } else {
                    alert("Invalid input. Please enter a valid number.");
                }
            }
            arr.push(num);
        }

        const descending = [...arr].sort((a, b) => b - a);
        const ascending = [...arr].sort((a, b) => a - b);
        document.writeln("<h2>Sorting</h2>");
        document.writeln("<hr>");
        document.writeln(`<p style="color: red;">u've entered the values of ${arr.join(',')}</p>`);
        document.writeln(`<p style="color: red;">ur values after being sorted descending ${descending.join(',')}</p>`);
        document.writeln(`<p style="color: red;">ur values after being sorted ascending ${ascending.join(',')}</p>`);
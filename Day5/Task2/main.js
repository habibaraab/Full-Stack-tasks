  const arr = [];
        for (let i = 0; i < 3; i++) {
            let num;
            while (true) {
                let input = prompt(`Enter number ${i + 1}:`);
                num = Number(input);
                if (!isNaN(num)) {
                    break;
                } else {
                    alert("Invalid input. Enter a valid number.");
                }
            }
            arr.push(num);
        }

        const sum = arr[0] + arr[1] + arr[2];
        const product = arr[0] * arr[1] * arr[2];
        const division = arr[0] / arr[1] / arr[2];
        document.writeln("<h2>Adding -- Multiplying -- and dividing 3 values</h2>");
        document.writeln("<hr>");
        document.writeln(
            `<p style="color: red;">
                sum of the 3 values ${arr[0]}+${arr[1]}+${arr[2]} = ${sum}
            </p>`
        );
        document.writeln(
            `<p style="color: red;">
                multiplication of the 3 values ${arr[0]}*${arr[1]}*${arr[2]} = ${product}
            </p>`
        );
    
        document.writeln(
            `<p style="color: red;">
                division of the 3 values ${arr[0]}/${arr[1]}/${arr[2]} = ${division}
            </p>`
        );
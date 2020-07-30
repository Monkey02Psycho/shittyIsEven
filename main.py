import subprocess

with open("even.rs", "w") as even:
    even.write("use std::io;")
    even.write("fn main(){\n")
    even.write("""
    let mut number = String::new();

    io::stdin()
        .read_line(&mut number)
        .expect("Failed to read line");

    println!("Check if {} is even", number);
    
    let number: u32 = number.trim().parse().expect("Please type a number!");

    match number{
    """)
    for i in range(0, 1000, 2):
        even.write("\t\t{} => println!(\"{{ }} is even\", number),\n".format(i))

    even.write("\t\t_ => println!(\"The number could be even\")}\n")
    even.write("\tloop{{}}\n")
    even.write("}")

subprocess.run(["rustc", "even.rs"])
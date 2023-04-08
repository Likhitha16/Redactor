import argparse
import main

if __name__ == "__main__":



    parser = argparse.ArgumentParser()
    parser.add_argument("--input",type = str, required = True, help = "Input files path" , nargs = "*", action = "append")
    parser.add_argument("--names", required = False, help = "Redacts names in input files", action = "store_true")
    parser.add_argument("--dates", required = False , help ="Redacts dates from input files", action = "store_true")
    parser.add_argument("--phones", required = False , help = "Redacts phone from input files " , action = "store_true")
    parser.add_argument("--genders", required = False , help = "Redacts genders from input files", action = "store_true")
    parser.add_argument("--address", required = False , help = "Redacts address from input files " , action = "store_true")
    parser.add_argument("--output",  type = str , required = True , help = "Output file path")
    parser.add_argument("--stats", type = str , required =True , help = "get stats from all the files ")

    args = parser.parse_args()

    source_data = main.read_input_files(args.input)

    if args.names:
        source_data = main.redact_names(source_data)

    if args.dates:
        source_data = main.redact_dates(source_data)
    
    if args.phones:
        source_data = main.redact_phone_numbers(source_data)

    if args.genders:
        source_data = main.redact_genders(source_data)
    if args.address:
        source_data = main.redact_address(source_data)
    if args.output:
        main.get_output_files(args.input,source_data,args.output)
    if args.stats:

        main.write_stats()

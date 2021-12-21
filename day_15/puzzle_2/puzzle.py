import sys
import os
import pprint
from datetime import datetime

initial_template = ''
template = ''
rule_array = []
pairs_array = []

def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath_rl = './input_file'
    filepath_tmpl = './input_file-template'

    if not os.path.isfile(filepath_rl):
        print("File path {} does not exist. Exiting...".format(filepath_rl))
        sys.exit()
    if not os.path.isfile(filepath_tmpl):
        print("File path {} does not exist. Exiting...".format(filepath_tmpl))
        sys.exit()

    ### Read the input into an array of integers
    read_array_in_template(filepath_tmpl)
    read_array_in_rules(filepath_rl)

    template = initial_template
    print("Original Template: {}".format(template))
    for k in range(2):
        tmpl = ''
        pairs_array = []

        template_pairs_zip = zip(template, template[1:])
        for a_, b_ in template_pairs_zip:
            pairs_array.append(a_+b_)
        
        template_pairs_zip = []
        template = ''
        # print("New pairs: ", pairs_array)

        end_ = ''
        for ab_ in pairs_array:
            # print("   Checking pair: ",ab_)
            ins_ = ''
            for pair, ins in rule_array:
                if ab_ == pair:
                    # print("   Found rule: ",pair, ins)
                    ins_ = ins
                    break
            tmpl += ab_[:1] + ins_
            end_ = ab_
        
        tmpl += end_[1:]
        # print("Template: {} - Length: {}".format(tmpl, len(tmpl)))
        # now = datetime.now()
        # dt_string = now.strftime("%H:%M:%S")
        # print("now =", now)
        # print("{} Template Length: {} - {}".format(k, len(tmpl), dt_string))
        template = tmpl
        
    elements = template[0]
    for elem_tmpl in template:
        if elem_tmpl not in elements:
            elements += elem_tmpl
    print("Elements: {}".format(elements))

    counter = 0
    min = 9999999999999
    max = 0
    for elem in elements:
        counter = 0
        for elem_tmpl in template:
            if elem == elem_tmpl:
                counter += 1
        print(elem, counter)
        if counter > max:
            max = counter
        if counter < min:
            min = counter

    


    print("================================================================")
    print("Result: {}".format(max-min))


### Iterate over the lines in the file
def read_array_in_template(filepath):
    global initial_template
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            initial_template = line.rstrip()
    print("Template: {}".format(initial_template))


### Iterate over the lines in the file
def read_array_in_rules(filepath):
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            elem_pair, elem_in = line.split(' -> ')
            rule_array.append([elem_pair, elem_in])
    pp.pprint(rule_array)

if __name__ == '__main__':
    main()
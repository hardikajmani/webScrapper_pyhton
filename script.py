

from robobrowser import RoboBrowser

br = RoboBrowser(history=True,parser='html.parser')
br.open("https://www.interntheory.com/affiliate")
form = br.get_form(action='https://www.interntheory.com/affiliate')

endCodes = ["", "1", "2", "3", "4", "5"]

for i in range(len(endCodes)):
    #print(endCodes[i])
    code = "ITR1040" + endCodes[i]
    form["affiliate"].value = code
    br.submit_form(form)

    data = br.select('div.form-group.col-md-6')
    print(data[0].text)
    entr = data[1].text
    print(entr)

def pdfModule(bytes):

    pdf = bytes
    # step 0: check locked pdf - Moses front and shivam back
    # step 1: temp save pdf - salah
    # step 2: breaking pdfs apart and saving imgs and logos - salah
        # step 2.1: make an array of images
        # step 2.2: algo to check all font in pdf (size,color,type)
        # step 2.3: create json for the pdf
    '''
        {
            img:{
                pageNumber:1
                index:1
                aiResponse:{
                    reponse: 85%
                    //comment:""
                }
                x:5,
                y:y
            }
            img2:{
                pageNumber:2
            }
        }
    '''
    # step 3: call the model to verify images and logos write to json - kelsey
    # step 4: calcuate average acc per image - computer
    # step 5: reconstruct the pdf based on the json file -shivam
    # step 6: send neat package back to the route to be sent to the frontend for proccesing - whoever
    return pdf



from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT


def iter_hyperlink_rels(rels):
    for rel in rels:
        if rels[rel].reltype == RT.HYPERLINK:
            yield rels[rel]._target


def main():
    document = Document(docx=r'C:\Users\Linc\Documents\discipline4boys.docx')
    rels = document.part.rels
    my_list = list(iter_hyperlink_rels(rels))
    # print("\n".join(my_list))
    print("Item count: {}".format(len(my_list)))
    for each in my_list:
        if "dropbox" in str(each):
            item = str(each)
            item = item.split("?z=")[1]
            item = item.replace("%3A",":")
            item = item.replace("%2F",r'/')
            print(item.split(r'&t=')[0])
            

if __name__ == '__main__':
    main()

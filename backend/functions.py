##################################
# Cristopher Barrios
# COMPILADORES 
##################################
# functions.py
##################################
import backend.classes as lista

def idTexto(id,stri,striLoop,valor,list_valus):
    countN = striLoop.count(id)
    indice_b = 0
    while countN > 0:
        indice_a = stri.find(id, indice_b) 
        indice_b = indice_a + 2
        value = stri[indice_a : indice_b]
        striLoop = striLoop.replace(value, '', 1)
        valus = lista.Valus(value,indice_a)
        valor.append(valus)
        list_valus.append(valus)
        
        countN = striLoop.count(id)

    return striLoop


def buscar_n_elemento(lista, e):
   contador=0
   for i in lista:
      if i == e:
         contador+=1
   return contador


def printidor(clases,metodos,ownmethod,property,formal,assignment,methodcall,ifcount,equal,lessequal,lessthan,minus,add,division,multiply,whileCount,declaration,letin,void,negative,boolnot,case,new,string,valor,block,id,parentheses,fals,integer,truet,instr,outstring,outint):
        print("\n\nCLASES:\n")
        for impClase in clases:
            impClase.get_clase_values()
            
        print("\n\nMETODOS:\n")
        for impMetodo in metodos:
            impMetodo.get_method_values()

        print("\n\nOWNmETHOD:\n")
        for impOWn in ownmethod:
            impOWn.get_omethod_values()

        print("\n\nPROPERTY:\n")
        for impOWn in property:
            impOWn.get_property_values()

        print("\n\nFORMAL:\n")
        for impOWn in formal:
            impOWn.get_formal_values()

        print("\n\nASSIGNMENT:\n")
        for impOWn in assignment:
            impOWn.get_assignment_values()

        print("\n\nMETHODCALL:\n")
        for impOWn in methodcall:
            impOWn.get_methodcall_values()

        print("\n\nIF:\n")
        for impOWn in ifcount:
            impOWn.get_ifcount_values()

        print("\n\nEqual:\n")
        for impOWn in equal:
            impOWn.get_equal_values()

        print("\n\nLessEqual:\n")
        for impOWn in lessequal:
            impOWn.get_lessequal_values()    

        print("\n\nLessThan:\n")
        for impOWn in lessthan:
            impOWn.get_lessthan_values()    

        print("\n\nMinus:\n")
        for impOWn in minus:
            impOWn.get_minus_values()

        print("\n\nAdd:\n")
        for impOWn in add:
            impOWn.get_add_values()    

        print("\n\nDivision:\n")
        for impOWn in division:
            impOWn.get_division_values()    

        print("\n\nMultiply:\n")
        for impOWn in multiply:
            impOWn.get_multiply_values()    

        print("\n\nWhileCount:\n")
        for impOWn in whileCount:
            impOWn.get_whilecount_values()    

        print("\n\nDecla:\n")
        for impOWn in declaration:
            impOWn.get_decla_values()    

        print("\n\nLetIn:\n")
        for impOWn in letin:
            impOWn.get_letin_values()    

        print("\n\nIsvoid:\n")
        for impOWn in void:
            impOWn.get_idvoid_values()    

        print("\n\nNegative:\n")
        for impOWn in negative:
            impOWn.get_negative_values()    

        print("\n\nBoolNot:\n")
        for impOWn in boolnot:
            impOWn.get_boolnot_values()    

        print("\n\nNew:\n")
        for impOWn in case:
            impOWn.get_case_values()    

        print("\n\nNew:\n")
        for impOWn in new:
            impOWn.get_new_values()    

        print("\n\nString:\n")
        for impOWn in string:
            impOWn.get_string_values()
        
        print("\n\nValor:\n")
        for impOWn in valor:
            impOWn.get_valus_values()   

        print("\n\nBlock:\n")
        for impOWn in block:
            impOWn.get_block_values()    

        print("\n\nId:\n")
        for impOWn in id:
            impOWn.get_id_values()    

        print("\n\nParentheses:\n")
        for impOWn in parentheses:
            impOWn.get_parentheses_values()    

        print("\n\nFalseCount:\n")
        for impOWn in fals:
            impOWn.get_falsecount_values()    

        print("\n\nInt:\n")
        for impOWn in integer:
            impOWn.get_int_values()    

        print("\n\nTrueCount:\n")
        for impOWn in truet:
            impOWn.get_truecoutn_values() 

        print("\n\nIn:\n")
        for impOWn in instr:
            impOWn.get_In_values() 

        print("\n\nOut_string:\n")
        for impOWn in outstring:
            impOWn.get_outstring_values() 

        print("\n\nOut_int:\n")
        for impOWn in outint:
            impOWn.get_outint_values() 
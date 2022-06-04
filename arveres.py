#Pedro Henrique Rossato RGM:23187808
#Adryann Layon Oliveira Lima RGM:23527081


class noDisciplina:
    def __init__(self,codigo,nome,nota):
        self.codigo=codigo
        self.nome=nome
        self.nota=nota
        self.esq=None
        self.dir=None
      
    def getCodigo(self):
        return self.codigo
    

    def getNome(self):
        return self.nome
    

    def setNome(self, nome):
        self.nome=nome

    
    def getNota(self):
        return self.nota
    def setNota(self, nota):
      self.nota=nota
    


    def getEsq(self):
        return self.esq


    def setEsq(self,esq):
        self.esq=esq
    

    def getDir(self):
        return self.dir


    def setDir(self,dir):
        self.dir=dir
      
class ArvoreDisciplina:
    def __init__(self):
        self.raiz=None

    def montaArvore(self,x,n,nota):
        if self.raiz==None:
            no=noDisciplina(x,n,nota)
            self.raiz=no
            return
        q=None
        p=self.raiz

        while p and p.codigo !=x :
            q=p
            if x < p.codigo:
                p=p.esq
            else:
                p=p.dir

        if p:
            print('dado ja cadastrado')
            return
        p=noDisciplina(x,n,nota)
        if x <q.codigo:
            q.esq=p
        else:
            q.dir=p

    def emOrdem(self,p):
        if p:
            self.emOrdem(p.esq)
            print(f' {p.codigo}  {p.nome}  {p.nota}')
            self.emOrdem(p.dir) 

    def alterarDisciplina(self, codigo, nome, nota):
      p = self.raiz
      while p and p.codigo != codigo:
        if p.getEsq().codigo <= codigo:
          p = p.getEsq()
        elif p.getDir().codigo <= codigo:
          p = p.getDir()
        else:
          p = None
      if p.codigo == codigo:
        p.nome = nome
        p.nota = nota
      else:
        print("Nao foi encotrado essa disciplina")
        
    def excluirDisciplina(self, x):
      p = self.raiz  #p recebe a raiz da arvore
      q = None

      while p and p.getCodigo() != x:
          q = p
          if x < p.getCodigo():  
              p = p.getEsq()
          else:
              p = p.getDir()

      if not p:
        print(f"Não cadastrado")
        return

     

      if not p.getEsq():
          v = p.getDir()
      elif not p.getDir():
          v = p.getEsq()
      else:

          t = p
          v = p.getDir()
          s = v.getEsq()
          while s:
              t = v
              v = s
              s = v.getEsq()

          if t != p:

              t.setEsq(v.getDir())
  
              v.setDir(p.getDir())
          v.setEsq(p.getEsq())
      if not q:
 
          self.raiz = v
      else:
          if p == p.getEsq():
              q.setEsq(v)
          else:
              q.setDir(v)
      p = None
          
      
    
class NoAluno:

    def __init__(self, codigo, nome, curso):
        self.codigo=codigo
        self.nome=nome
        self.curso=curso
        self.esq=None
        self.dir=None
        self.arvore=ArvoreDisciplina()
    
    def getCodigo(self):
        return self.codigo
    

    def getNome(self):
        return self.nome
    

    def setNome(self, nome):
        self.nome=nome

    
    def getCurso(self):
        return self.curso
    def setCurso(self, curso):
      self.curso=curso
    


    def getEsq(self):
        return self.esq


    def setEsq(self,esq):
        self.esq=esq
    

    def getDir(self):
        return self.dir


    def setDir(self,dir):
        self.dir=dir



class Arvore:
    def __init__(self):
        self.raiz=None

   
    def montaArvore(self, codigo, nome, curso):
        if self.raiz==None:
            no=NoAluno(codigo, nome, curso)
            self.raiz=no
            return

        q = None
        p = self.raiz
        while p and p.getCodigo() != codigo:
            q = p
            if codigo < p.getCodigo():
                p = p.getEsq()
            else:
                p = p.getDir()
        
        if p:
            print('Já Cadastrado(a)')
            return
        p = NoAluno(codigo, nome, curso)
        if codigo < q.getCodigo():
            q.setEsq(p)
        else:
            q.setDir(p)

        


    def emOrdem(self,p):
        if p:
            self.emOrdem(p.getEsq())
            print(f'Nó visitado em emOrdem: {p.getCodigo(), p.getNome(), p.getCurso()}')
            self.emOrdem(p.getDir())
    
    
    def removeNo(self, codigo):
        p = self.raiz
        q = None
        while p and p.getCodigo() != codigo:
            q = p
            if codigo < p.getCodigo():
                p = p.getEsq()
            else:
                p = p.getDir()

        if not p:
            print('Não cadastrado')
            return
        if p.arvore.raiz:
          print("Nao foi possivel excluir aluno pois ele possui uma disciplina")
          return
        
        if not p.getEsq():
            v = p.getDir()
        elif not p.getDir():
            v = p.getEsq()
        else:
            t = p
            v = p.getDir()
            s = v.getEsq()
            while s:
                t = v
                v = s
                s = v.getEsq()
            if t != p:
                t.setEsq(v.getDir())
            v.setDir(p.getEsq())
        
        if not q:
            self.raiz = v
        else:
            if p == q.getEsq():
                q.setEsq(v)
            else:
                q.setDir(v)
        p = None

    def replace(self, codigo, nome, curso,p):
      if p:
        self.replace(codigo, nome, curso, p.getEsq())
        if p.getCodigo() == codigo:
          p.setNome(nome)
          p.setCurso(curso)
        self.replace(codigo, nome, curso, p.getDir())
        
      

    
    def pesquisarNo(self, codigo, p):
         if p == None:
            return None 
         if p.getCodigo() == codigo:
           return p
         if p.getCodigo() < codigo:
           return self.pesquisarNo(codigo, p.getDir())
         if p.getCodigo() > codigo:
           return self.pesquisarNo(codigo, p.getEsq())

  
    def relatorioCurso(self, p, nomeCurso):
      if p:
        self.relatorioCurso(p.getEsq(), nomeCurso)
        if p.getCurso() == nomeCurso:
          print(p.getCodigo(), p.getNome(), p.getCurso() )
        self.relatorioCurso(p.getDir(), nomeCurso)

    def obtemAluno(self, codigoAluno):
           p = self.raiz
           while p and p.codigo != codigoAluno:
              q = p
              if (codigoAluno < p.codigo):
                  p = p.esq
              else:
                  p = p.dir
  
           return p
          
    def incluiDisciplina(self, codigoAluno, codigo, nome, nota):
        p = self.obtemAluno(codigoAluno)
        if not p:
            print('aluno nao encontrado')
            return
        disc = p.arvore
        disc.montaArvore(codigo, nome, nota)

    def mostraAlunoNota(self, p):
        if p:
            self.mostraAlunoNota(p.esq)
            print(f'Aluno: {p.codigo}   {p.nome}   {p.curso}')
            p.arvore.emOrdem(p.arvore.raiz)
            self.mostraAlunoNota(p.dir)
        

    def alteraDisciplina(self, codigoAluno, codigo, nome, nota ):
      p = self.obtemAluno(codigoAluno)
      if not p:
          print('aluno nao encontrado')
          return
      disc = p.arvore
      disc.alterarDisciplina(codigo, nome, nota)

    
    def excluirDisciplina(self, codigoAluno, codigoDisciplina):
      aluno = self.obtemAluno(codigoAluno)
      if not aluno:
        print("Aluno nao encontrado")
      aluno.arvore.excluirDisciplina(codigoDisciplina)

      
arv=Arvore()
arv.montaArvore(50,'teste50', 'teste50')
arv.montaArvore(1,'teste1', 'teste2')
arv.montaArvore(2,'teste2', 'teste2')
arv.montaArvore(3,'teste3', 'teste3')
arv.removeNo(3)
arv.emOrdem(arv.raiz)     
arv.pesquisarNo(2, arv.raiz)
nn = "aa"
nc = "aa1"
cod = 50
arv.replace(cod,nn,nc, arv.raiz)
print()
arv.emOrdem(arv.raiz)  
print()
arv.relatorioCurso(arv.raiz, "teste2")
print()
arv.incluiDisciplina(50,50,'SI', '10')
arv.incluiDisciplina(1,1, 'Design', '5')
arv.incluiDisciplina(2,2, 'Engenharia', '6')
arv.incluiDisciplina(3,3, 'Marketing', '10')
arv.mostraAlunoNota(arv.raiz)
print()
arv.alteraDisciplina(1,1,"1111", "0")
arv.mostraAlunoNota(arv.raiz)

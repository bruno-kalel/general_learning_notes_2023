package course_java_aplicando_orientacao_objetos.modelos.src;

import course_java_aplicando_orientacao_objetos.modelos.modelos.Filme;

public class Principal
{
    public static void main(String[] args)
    {
        Filme rearWindow = new Filme();

        rearWindow.setNome("Rear Window");
        rearWindow.setAnoDeLançamento(1954);
        rearWindow.setDuraçãoEmMinutos(112);

        rearWindow.exibeFichaTécnica();

        rearWindow.avalia(10);
        rearWindow.avalia(9.5);
        rearWindow.avalia(9.0);

        System.out.println(rearWindow.getTotalDeAvaliações());
        System.out.println(rearWindow.pegaMédiaDasAvaliações());
    }
}

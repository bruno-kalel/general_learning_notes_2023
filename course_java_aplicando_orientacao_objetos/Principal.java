public class Principal
{
    public static void main(String[] args)
    {
        Filme rearWindow = new Filme();
        rearWindow.nome = "Rear Window";
        rearWindow.anoDeLançamento = 1954;
        rearWindow.duraçãoEmMinutos = 112;

        rearWindow.exibeFichaTécnica();

        rearWindow.avalia(10);
        rearWindow.avalia(9.5);
        rearWindow.avalia(9.0);

        System.out.println(rearWindow.somaDasAvaliações);
        System.out.println(rearWindow.totalDeAvaliações);
        System.out.println(rearWindow.pegaMédiaDasAvaliações());
    }
}

public class Principal
{
    public static void main(String[] args)
    {
        Filme filme1 = new Filme();
        filme1.setNome("Rear Window");
        filme1.setAnoDeLançamento(1954);
        filme1.setDuraçãoEmMinutos(112);
        filme1.exibeFichaTécnica();
        filme1.avalia(10);
        filme1.avalia(9);
        filme1.pegaMédiaDasAvaliações();

        Filme filme2 = new Filme();
        filme2.setNome("Ferris Bueller’s Day Off");
        filme2.setAnoDeLançamento(1986);
        filme2.setDuraçãoEmMinutos(103);
        filme2.exibeFichaTécnica();
        filme2.avalia(9);
        filme2.avalia(8);
        filme2.pegaMédiaDasAvaliações();

        Série série1 = new Série();
        série1.setTemporadas(5);
        série1.setEpisódiosPorTemporada(5);
        série1.setMinutosPorEpisódio(50);

        Série série2 = new Série();
        série2.setTemporadas(10);
        série2.setEpisódiosPorTemporada(10);
        série2.setMinutosPorEpisódio(25);

        CalculadoraDeTempo calculadoraDeTempo = new CalculadoraDeTempo();
        calculadoraDeTempo.inclui(filme1);
        calculadoraDeTempo.inclui(filme2);
        calculadoraDeTempo.inclui(série1);
        calculadoraDeTempo.inclui(série2);

        System.out.println(calculadoraDeTempo.getTempoTotal());

        FiltroDeRecomendação filtroDeRecomendação = new FiltroDeRecomendação();
        filtroDeRecomendação.filtra(filme1);
        filtroDeRecomendação.filtra(filme2);

        Episódio episódio = new Episódio();
        episódio.setTotalDeVisualizações(300);

        filtroDeRecomendação.filtra(episódio);
    }
}
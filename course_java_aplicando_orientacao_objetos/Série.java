public class Série extends Título
{
    private int temporadas;
    private int episódiosPorTemporada;
    private int minutosPorEpisódio;

    public void setTemporadas(int temporadas)
    {
        this.temporadas = temporadas;
    }

    public void setEpisódiosPorTemporada(int episódiosPorTemporada)
    {
        this.episódiosPorTemporada = episódiosPorTemporada;
    }

    public void setMinutosPorEpisódio(int minutosPorEpisódio)
    {
        this.minutosPorEpisódio = minutosPorEpisódio;
    }

    @Override
    public int getDuraçãoEmMinutos()
    {
        return temporadas * episódiosPorTemporada * minutosPorEpisódio;
    }
}
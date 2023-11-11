public class CalculadoraDeTempo
{
    private int tempoTotal;

    public int getTempoTotal()
    {
        return tempoTotal;
    }

    public void inclui(Título título)
    {
        tempoTotal += título.getDuraçãoEmMinutos();
    }
}
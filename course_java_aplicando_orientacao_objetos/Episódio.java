public class Episódio implements Classificável
{
    private int totalDeVisualizações;

    public void setTotalDeVisualizações(int totalDeVisualizações)
    {
        this.totalDeVisualizações = totalDeVisualizações;
    }

    @Override
    public int getClassificação()
    {
        if (totalDeVisualizações > 100)
        {
            return 4;
        }
        return 2;
    }
}
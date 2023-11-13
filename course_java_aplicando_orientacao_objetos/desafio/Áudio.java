public class Áudio implements Reproduzível
{
    private String título;
    private int duraçãoEmSegundos;
    private int totalDeReproduções;
    private int totalDeCurtidas;

    public String getTítulo()
    {
        return título;
    }

    public void setTítulo(String título)
    {
        this.título = título;
    }

    public int getDuraçãoEmSegundos()
    {
        return duraçãoEmSegundos;
    }

    public void setDuraçãoEmSegundos(int duraçãoEmSegundos)
    {
        this.duraçãoEmSegundos = duraçãoEmSegundos;
    }

    public void curtir()
    {
        System.out.println("Curtindo...");
        totalDeCurtidas++;
        System.out.println("totalDeCurtidas: " + totalDeCurtidas);
    }

    public void reproduzir()
    {
        System.out.println("Reproduzindo...");
        totalDeReproduções++;
        System.out.println("totalDeReproduções: " + totalDeReproduções);
    }
}

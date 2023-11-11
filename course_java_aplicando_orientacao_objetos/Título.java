public class Título
{
    private String nome;
    private int anoDeLançamento;
    private int duraçãoEmMinutos;
    private double somaDasAvaliações;
    private int totalDeAvaliações;

    public void setNome(String nome)
    {
        this.nome = nome;
    }

    public void setAnoDeLançamento(int anoDeLançamento)
    {
        this.anoDeLançamento = anoDeLançamento;
    }

    public int getDuraçãoEmMinutos()
    {
        return duraçãoEmMinutos;
    }

    public void setDuraçãoEmMinutos(int duraçãoEmMinutos)
    {
        this.duraçãoEmMinutos = duraçãoEmMinutos;
    }

    public void exibeFichaTécnica()
    {
        System.out.println("nome: " + nome);
        System.out.println("anoDeLançamento: " + anoDeLançamento);
        System.out.println("duraçãoEmMinutos: " + duraçãoEmMinutos);
    }

    public void avalia(double nota)
    {
        somaDasAvaliações += nota;
        totalDeAvaliações++;
    }

    public double pegaMédiaDasAvaliações()
    {
        return somaDasAvaliações / totalDeAvaliações;
    }
}
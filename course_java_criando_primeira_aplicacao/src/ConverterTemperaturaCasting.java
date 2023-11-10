public class ConverterTemperaturaCasting
{
    public static void main(String[] args)
    {
        double grausCelsius = 40;
        int grausFahrenheit = (int) ((grausCelsius * 1.8) + 32);
        System.out.println(grausFahrenheit);
    }
}
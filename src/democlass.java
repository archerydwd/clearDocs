/*
 *This is a demo class comment that describes the DemoClass class.
 *
 * @author Darren Daly
 * @version 1.0
 * @since 2015-01-28
*/
public class DemoClass
{
	private int x;

	public DemoClass()
	{
		x = 0;
	}
	public DemoClass(int x)
	{
		this.x = x;
	}
	public DemoClass(double x, int x)
	{
		this.x = x;
	}
	public DemoClass(DemoClass otherDemo)
	{
		this.x = otherDemo.x;
	}
	private double mul(double a, double b) 
	{
		return a * b;
	}
	private static void i2() 
	{
		s1();
		i1();
		return;
	}
	public void overloadTester() 
	{
		System.out.println("overloadTester:\n");

		overload((byte)1);
		overload((short)1);
		overload(1);
		overload(1L);
		overload(1.0f);
		overload(1.0);
		overload('1');
		overload(true);
	}
	/*
	 * Description of method.
	 * 
	 * @param byte b
	 * @return void
	 */
	public void overload(byte b) 
	{
		System.out.println("byte");
	}    
	public void overload(short s) 
	{
		System.out.println("short");
	}    
	public void overload(int i) 
	{
		System.out.println("int");
	}
	public void overload(long l) 
	{
		System.out.println("long");
	}
	public void overload(float f) {
		System.out.println("float");
	}
	public void overload(double d) 
	{
		System.out.println("double");
	}    
	public void overload(char c) 
	{
		System.out.println("char");
	}    
	public void overload(boolean b) 
	{
		System.out.println("boolean");
	}    
	public static void main(String[] args) 
	{
		DemoClass dc = new DemoClass();
		dc.overloadTester();
	}
}
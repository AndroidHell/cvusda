short int reverse_byte_order(short int);

class MLX{
private:
  int fd;
  double temp;
  short unsigned int msg;
public:
  double readTemp(); 
  MLX(void);
  ~MLX(void);
};

using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    public interface IAuthValidation
    {
        bool IsValidated(AuthInfo info, int coefficient);
    }
}

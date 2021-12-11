using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    public interface IAuthValidationSource
    {
        bool Check(AuthInfo authInfo, int coefficient);
    }
}

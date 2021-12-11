using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    public class DbValidationSource : IAuthValidationSource
    {
        public bool Check(AuthInfo authInfo, int coefficient) => false;
    }
}

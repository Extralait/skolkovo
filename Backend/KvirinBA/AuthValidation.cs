using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    public class AuthValidation : IAuthValidation
    {
        private IAuthValidationSource _source;

        public AuthValidation(IAuthValidationSource source) => this._source = source;

        public bool IsValidated(AuthInfo info, int coefficient) => this._source.Check(info, coefficient);
    }
}

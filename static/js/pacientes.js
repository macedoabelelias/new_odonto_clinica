// =========================================
// MÁSCARA CPF
// =========================================

function maskCPF(inputId){

    const input = document.getElementById(inputId);

    if(!input) return;

    input.addEventListener('input', function(e){

        let value = e.target.value.replace(/\D/g,'');

        // LIMITE

        value = value.substring(0,11);

        value = value.replace(/(\d{3})(\d)/,'$1.$2');

        value = value.replace(/(\d{3})(\d)/,'$1.$2');

        value = value.replace(/(\d{3})(\d{1,2})$/,'$1-$2');

        e.target.value = value;

    });

}

maskCPF('cpf');

maskCPF('cpf_responsavel');

// =========================================
// TELEFONE
// =========================================

function maskPhone(inputId){

    const input = document.getElementById(inputId);

    if(!input) return;

    input.addEventListener('input', function(e){

        let value = e.target.value.replace(/\D/g,'');

        // LIMITE

        value = value.substring(0,11);

        value = value.replace(/^(\d{2})(\d)/g,'($1) $2');

        value = value.replace(/(\d)(\d{4})$/,'$1-$2');

        e.target.value = value;

    });

}

maskPhone('telefone');

maskPhone('whatsapp');

maskPhone('telefone_responsavel');

// =========================================
// CEP
// =========================================

const cepInput = document.getElementById('cep');

if(cepInput){

    cepInput.addEventListener('input', function(e){

        let value = e.target.value;

        value = value.replace(/\D/g,'');

        value = value.replace(/^(\d{5})(\d)/,'$1-$2');

        e.target.value = value;

    });

}


// =========================================
// VIA CEP
// =========================================

cepInput?.addEventListener('blur', async function(){

    const cep = this.value.replace(/\D/g,'');

    if(cep.length !== 8){

        return;

    }

    try{

        const response = await fetch(

            `https://viacep.com.br/ws/${cep}/json/`

        );

        const data = await response.json();

        if(data.erro){

            return;

        }

        document.getElementById('endereco').value = data.logradouro || '';

        document.getElementById('bairro').value = data.bairro || '';

        document.getElementById('cidade').value = data.localidade || '';

        document.getElementById('estado').value = data.uf || '';

    }

    catch(error){

        console.log(error);

    }

});

// =========================================
// DATA NASCIMENTO
// =========================================

const nascimentoInput = document.querySelector(

    'input[name="nascimento"]'

);

if(nascimentoInput){

    nascimentoInput.addEventListener('change', function(){

        const hoje = new Date();

        const nascimento = new Date(this.value);

        // BLOQUEIA FUTURO

        if(nascimento > hoje){

            alert(

                'Data de nascimento inválida.'

            );

            this.value = '';

            return;

        }

        // CALCULAR IDADE

        let idade = hoje.getFullYear()

        - nascimento.getFullYear();

        const mes = hoje.getMonth()

        - nascimento.getMonth();

        if(

            mes < 0 ||

            (
                mes === 0 &&
                hoje.getDate() < nascimento.getDate()
            )

        ){

            idade--;

        }

        // MOSTRAR IDADE

const idadeInput = document.getElementById('idade');

if(idadeInput){

    idadeInput.value = idade;

}

        // RESPONSÁVEL

        const responsavelSection = document.querySelector(

            '.responsavel-section'

        );

        if(responsavelSection){

            if(idade < 18){

                responsavelSection.style.display = 'block';

            }

            else{

                responsavelSection.style.display = 'none';

            }

        }

    });

}

// =========================================
// PREVIEW FOTO
// =========================================

const fotoInput = document.querySelector(

    'input[name="foto"]'

);

if(fotoInput){

    fotoInput.addEventListener('change', function(e){

        const file = e.target.files[0];

        if(!file) return;

        const reader = new FileReader();

        reader.onload = function(event){

            const preview = document.getElementById(

                'previewFoto'

            );

            const icon = document.getElementById(

                'cameraIcon'

            );

            preview.src = event.target.result;

            preview.style.display = 'block';

            icon.style.display = 'none';

        }

        reader.readAsDataURL(file);

    });

}

// =========================================
// VALIDAR CPF
// =========================================

function validarCPF(cpf){

    cpf = cpf.replace(/\D/g,'');

    // TAMANHO

    if(cpf.length !== 11){

        return false;

    }

    // CPFs INVÁLIDOS

    if(/^(\d)\1+$/.test(cpf)){

        return false;

    }

    let soma = 0;

    let resto;

    // PRIMEIRO DÍGITO

    for(let i=1; i<=9; i++){

        soma += parseInt(cpf.substring(i-1,i))

        * (11 - i);

    }

    resto = (soma * 10) % 11;

    if(resto === 10 || resto === 11){

        resto = 0;

    }

    if(resto !== parseInt(cpf.substring(9,10))){

        return false;

    }

    soma = 0;

    // SEGUNDO DÍGITO

    for(let i=1; i<=10; i++){

        soma += parseInt(cpf.substring(i-1,i))

        * (12 - i);

    }

    resto = (soma * 10) % 11;

    if(resto === 10 || resto === 11){

        resto = 0;

    }

    if(resto !== parseInt(cpf.substring(10,11))){

        return false;

    }

    return true;

}


// =========================================
// FEEDBACK CPF
// =========================================

function feedbackCPF(inputId){

    const input = document.getElementById(inputId);

    if(!input) return;

    input.addEventListener('blur', function(){

        const value = this.value;

        // LIMPO

        this.classList.remove(

            'is-invalid',
            'is-valid'

        );

        if(value.length < 14){

            return;

        }

        if(validarCPF(value)){

            this.classList.add('is-valid');

        }

        else{

            this.classList.add('is-invalid');

        }

    });

}

feedbackCPF('cpf');

feedbackCPF('cpf_responsavel');
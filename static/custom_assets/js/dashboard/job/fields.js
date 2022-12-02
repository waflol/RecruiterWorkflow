let editor;
DecoupledEditor
    .create(document.querySelector('#kt_ckeditor_description'),{
        ckfinder: {
            uploadUrl: '/ckeditor/upload/'
        },
    })
    .then(newEditor => {
        editor = newEditor;
        const toolbarContainer = document.querySelector( '#kt_ckeditor_description_toolbar' );
        console.log( 'Editor was initialized', editor );
        toolbarContainer.appendChild( editor.ui.view.toolbar.element );
    })
    .catch(error => {
        console.error(error);
    });

DecoupledEditor
    .create(document.querySelector('#kt_ckeditor_requirement'),{
        ckfinder: {
            uploadUrl: '/ckeditor/upload/'
        },
    })
    .then(newEditor => {
        editor = newEditor;
        const toolbarContainer = document.querySelector( '#kt_ckeditor_requirement_toolbar' );
        console.log( 'Editor was initialized', editor );
        toolbarContainer.appendChild( editor.ui.view.toolbar.element );
    })
    .catch(error => {
        console.error(error);
    });

DecoupledEditor
    .create(document.querySelector('#kt_ckeditor_right'),{
        ckfinder: {
            uploadUrl: '/ckeditor/upload/'
        },
    })
    .then(newEditor => {
        editor = newEditor;
        const toolbarContainer = document.querySelector( '#kt_ckeditor_right_toolbar' );
        console.log( 'Editor was initialized', editor );
        toolbarContainer.appendChild( editor.ui.view.toolbar.element );
    })
    .catch(error => {
        console.error(error);
    });

$(".js-datepicker").flatpickr({
    minDate: "today",
    altInput: true,
    altFormat: "d/m/Y",
    dateFormat: "Y-m-d",
});

$('#kt_docs_repeater_basic').repeater({
    initEmpty: false,

    defaultValues: {
        'text-input': 'foo'
    },

    show: function () {
        $(this).slideDown();
    },

    hide: function (deleteElement) {
        $(this).slideUp(deleteElement);
    }
});

let job_type_input = document.querySelector('#job_type');

// Init Tagify script on the above inputs
tagify_job_type = new Tagify(job_type_input, {
    whitelist: ["FullTime", "PartTime", "Internship", "Freelancer"],
    placeholder: "Type something",
    enforceWhitelist: true,
    maxTags: 4,
});

// Suggestions
let suggestions = document.querySelector('#kt_tagify_job_type');

// Suggestion item click
KTUtil.on(suggestions,  '[data-kt-suggestion="true"]', 'click', function(e) {
    tagify_job_type.addTags([this.innerText]);
});

let job_category_input = document.querySelector('#job_category');
    // init Tagify script on the above inputs
new Tagify(job_category_input, {
    whitelist: ["A# .NET", "A# (Axiom)", "A-0 System", "A+", "A++", "ABAP", "ABC", "ABC ALGOL", "ABSET", "ABSYS", "ACC", "Accent", "Ace DASL", "ACL2", "Avicsoft", "ACT-III", "Action!", "ActionScript", "Ada", "Adenine", "Agda", "Agilent VEE", "Agora", "AIMMS", "Alef", "ALF", "ALGOL 58", "ALGOL 60", "ALGOL 68", "ALGOL W", "Alice", "Alma-0", "AmbientTalk", "Amiga E", "AMOS", "AMPL", "Apex (Salesforce.com)", "APL", "AppleScript", "Arc", "ARexx", "Argus", "AspectJ", "Assembly language", "ATS", "Ateji PX", "AutoHotkey", "Autocoder", "AutoIt", "AutoLISP / Visual LISP", "Averest", "AWK", "Axum", "Active Server Pages", "ASP.NET", "B", "Babbage", "Bash", "BASIC", "bc", "BCPL", "BeanShell", "Batch (Windows/Dos)", "Bertrand", "BETA", "Bigwig", "Bistro", "BitC", "BLISS", "Blockly", "BlooP", "Blue", "Boo", "Boomerang", "Bourne shell (including bash and ksh)", "BREW", "BPEL", "B", "C--", "C++ – ISO/IEC 14882", "C# – ISO/IEC 23270", "C/AL", "Caché ObjectScript", "C Shell", "Caml", "Cayenne", "CDuce", "Cecil", "Cesil", "Céu", "Ceylon", "CFEngine", "CFML", "Cg", "Ch", "Chapel", "Charity", "Charm", "Chef", "CHILL", "CHIP-8", "chomski", "ChucK", "CICS", "Cilk", "Citrine (programming language)", "CL (IBM)", "Claire", "Clarion", "Clean", "Clipper", "CLIPS", "CLIST", "Clojure", "CLU", "CMS-2", "COBOL – ISO/IEC 1989", "CobolScript – COBOL Scripting language", "Cobra", "CODE", "CoffeeScript", "ColdFusion", "COMAL", "Combined Programming Language (CPL)", "COMIT", "Common Intermediate Language (CIL)", "Common Lisp (also known as CL)", "COMPASS", "Component Pascal", "Constraint Handling Rules (CHR)", "COMTRAN", "Converge", "Cool", "Coq", "Coral 66", "Corn", "CorVision", "COWSEL", "CPL", "CPL", "Cryptol", "csh", "Csound", "CSP", "CUDA", "Curl", "Curry", "Cybil", "Cyclone", "Cython", "Java", "Javascript", "M2001", "M4", "M#", "Machine code", "MAD (Michigan Algorithm Decoder)", "MAD/I", "Magik", "Magma", "make", "Maple", "MAPPER now part of BIS", "MARK-IV now VISION:BUILDER", "Mary", "MASM Microsoft Assembly x86", "MATH-MATIC", "Mathematica", "MATLAB", "Maxima (see also Macsyma)", "Max (Max Msp – Graphical Programming Environment)", "Maya (MEL)", "MDL", "Mercury", "Mesa", "Metafont", "Microcode", "MicroScript", "MIIS", "Milk (programming language)", "MIMIC", "Mirah", "Miranda", "MIVA Script", "ML", "Model 204", "Modelica", "Modula", "Modula-2", "Modula-3", "Mohol", "MOO", "Mortran", "Mouse", "MPD", "Mathcad", "MSIL – deprecated name for CIL", "MSL", "MUMPS", "Mystic Programming L"],
    maxTags: 10,
    dropdown: {
        maxItems: 20,           // <- mixumum allowed rendered suggestions
        classname: "tags-look", // <- custom classname for this dropdown, so it could be targeted
        enabled: 0,             // <- show suggestions on focus
        closeOnSelect: false    // <- do not hide the suggestions dropdown once an item has been selected
    }
});

function getRepeaterData(id_repeater) {
    let items = $(id_repeater).find("[data-repeater-item]");
    items.toArray().map((item) =>{
        let inputs = item.querySelectorAll('input');
        let object = {
            'order': inputs[0].value,
            'name': inputs[1].value
        }
        console.log(object);
    })
}
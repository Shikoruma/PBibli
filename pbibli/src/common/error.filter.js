export function errorValue(value){
    var str=""
    if(Array.isArray(value)){
        for(var k in value)
        {
            str+=value[k]
        }
    }else if(typeof value === 'string' || value instanceof String)
    {
        str=value
    }
    else if(Object.keys(value).length != 0){
        for(var k in value)
        {
            str+=" "+k+" "+value[k]
        }   
    }
    else{
        str=value
    }
    return `${str}`;
};
export function errorKey(key){
    if (key == 'non_field_errors')
        return ""
    return `${key}`;
};

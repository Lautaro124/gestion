import { type InputTypeProp } from '~/interface/inputType'

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  styleProp?: InputTypeProp
  error?: string
  validate?: (value: string) => string | undefined
}

const Input = ({ styleProp, error, validate, ...restOfProps }: InputProps) => {
  const className = styleProp === 'line'
    ? 'border-b-2 border-blue-500 border-opacity-50 focus:border-blue-500 focus:ring-0 focus:border-opacity-100 focus:outline-none'
    : 'border-2 border-blue-500 border-opacity-50 focus:border-blue-500 focus:ring-0 focus:border-opacity-100 focus:outline-none'

  return <input className={className} {...restOfProps} />
}

export default Input
